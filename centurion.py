# Command handling module -  used for call-response type commands and interfacing with local data
# Returns info to the driver as a string in the form 'action user responseMsg'
# valid actions: ban timeout purge unban respond none
# Expects info in form 'username highestRole command args'
# Valid roles for module ( may need to be altered by main service interface)
# Caster Mod Sub Follower Normal (in descending order)
import sys, json, datetime
import pymysql
import ganon

builtins = ["!permit","!add","!ban","!purge","!timeout","!unban","!remove","!deathblossom"]
roles = ["Caster","Mod","Sub","Follower","Normal"]
conn = None
dbAddr = ""
dbUser = ""
dbPass = ""
db = ""
debug = False

#Get the config data
def loadConfig(configPath):
    global dbAddr, dbPass, dbUser, db, debug, CONFIG_PATH
    CONFIG_PATH = configPath
    with open(configPath) as data:
        config = json.load(data)
        debug = config["debug"]
        dbAddr = config["databaseURL"]
        dbPass = config["databasePassword"]
        dbUser = config["databaseUser"]
        db = config["databaseName"]
        data.close()
    ganon.loadConfig(CONFIG_PATH)

#returns an array of the three inputs
#eg [username, role, message]
def read_in():
    lines = sys.stdin.readlines()
    line = lines[0].strip()
    return line.split(maxsplit=3)

#returns the user and the response to the command
def parseCommand(input):
    global builtins
    user = input[0]
    role = input[1]
    command = input[2]
    args = None
    try:
        args = input[3]
    except IndexError as e:
        args = ""
    if command in builtins:
        if command == "!add":
            if role != "Caster" and role !="Mod":
                return "none", user, ""
            argArr = args.split(maxsplit=2) #Args are newCmd reqRole response
            try:
                newCmd = argArr[0]
                reqRole = argArr[1]
                if not reqRole in roles:
                    return "respond", user, "Invalid new command. Expected Format: '!newCmd requiredRole response'"
                newResponse = argArr[2]
                if store(newCmd,newResponse,reqRole): #TODO move this logic to the store cmd?
                    return "respond", user, "New command {} successfully stored".format(newCmd)
                else:
                    return "respond", user, "Error storing new command in database"
            except IndexError as e:
                if debug:
                    print(e, file=sys.stderr)
                return "respond", user, "Invalid new command. Expected Format: '!newCmd requiredRole response'"
        elif command == "!remove":
            if role != "Caster" and role !="Mod":
                return "none", user, ""
            testResp, testRole, lastUsed = retrieve(args)
            if testResp == None:
                return "respond", user, "That command does not exist"
            else:
                if delete(args):
                    return "respond", user, "Command {} successfully removed".format(args)
                else:
                    return "respond", user, "Error removing command {} in database".format(args)
        elif command == "!purge":
            if role != "Caster" and role !="Mod":
                return "none", user, "Required Role not met"
            if args != None and args != "" and args.find(" ")==-1:
                return "purge", args, "Purging user: " + args
            else:
                return "none", user, "Invalid Args"
        elif command == "!timeout":
            if role != "Caster" and role !="Mod":
                return "none", user, "Required Role not met"
            if args != None and args != "" and args.find(" ")==-1:
                return "timeout", args, "Timing out user: " + args
            else:
                return "none", user, "Invalid Args"
        elif command == "!ban":
            if role != "Caster" and role !="Mod":
                return "none", user, "Required Role not met"
            if args != None and args != "" and args.find(" ")==-1:
                return "ban", args, "Banning user: " + args
            else:
                return "none", user, "Invalid Args"
        elif command == "!unban":
            if role != "Caster" and role !="Mod":
                return "none", user, "Required Role not met"
            if args != None and args != "" and args.find(" ")==-1:
                return "unban", args, "Unbanning user: " + args
            else:
                return "none", user, "Invalid Args"
        elif command == "!permit":
            if role != "Caster" and role !="Mod":
                return "none", user, "Required Role not met"
            if args != None and args != "" and args.find(" ")==-1:
                if ganon.addPermits(args):
                    return "respond", args, "User " + args + " is allowed to post 1 link in the next 10 minutes"
                else:
                    return "respond", args, "Error permiting user"
            else:
                return "none", user, "Invalid Args"
        elif command == "!deathblossom":
            if role != "Caster" and role !="Mod":
                return "none", user, "Required Role not met"
            return "deathblossom", user, "Toggled deathblossom mode"
    else:
        response, neededRole, lastUsed = retrieve(command) #returns None, 'Root' if not in DB

        #see if the command is on cooldown
        if lastUsed == None:
            onCooldown = False
        else:
            onCooldown = lastUsed + datetime.timedelta(minutes=5) > datetime.datetime.utcnow()

        if hasAccess(role,neededRole) and response != None and (not onCooldown or role == "Mod" or role == "Caster"):
            updateLastUsed(command)
            return "respond", user, response
        else:
            return "none", user, ""


def updateLastUsed(command):
    #Load globals needed
    global conn, debug

    #make sure we have a connection to DB
    if conn == None:
        connect()

    #Make the SQL statement
    update = "UPDATE commands SET lastUsed=%s WHERE command = %s"
    time = datetime.datetime.utcnow()
    timeStr = ganon.pythonToString(time)

    #Create cursor to execute query
    cursor = conn.cursor()

    try:
        cursor.execute(update, (command, timeStr))
        conn.commit()
        return True
    except Excetion as e:
        if debug:
            print(e)
        conn.rollback()
        return False

def retrieve(command):
    #Load globals needed
    global conn
    #prepare default return values
    response = None
    lastUsed = None
    neededRole = 'Root'
    retrivedCommand = command

    #debug text
    if debug:
        print("Command is: " + command, file=sys.stderr)

    #make the SQL statement
    query = "SELECT command, role, response, lastUsed FROM commands WHERE command=%s"
    #make sure we have a connection to the DB
    if conn == None:
        connect()
    #create a cursor to execute SELECT query
    cursor = conn.cursor()
    cursor.execute(query, (command))
    results = cursor.fetchone()

    try:
        #store results in the return vals
        lastUsed = results[3]
        response = results[2]
        neededRole = results[1]
        retrivedCommand = results[0]
    except Exception as e:
        if debug:
            print(e, file=sys.stderr)

    if debug:
        print("SQL is: " + query.format(command), file=sys.stderr)
        print(retrivedCommand, file=sys.stderr)
        print(response, file=sys.stderr)
        print(neededRole, file=sys.stderr)


    return response, neededRole, lastUsed

def retrieveList(role):
    #Load globals needed
    global conn
    #prepare default return values
    commands = []


    #make the SQL statement
    query = "SELECT command FROM commands WHERE role=%s"
    #make sure we have a connection to the DB
    if conn == None:
        connect()
    #create a cursor to execute SELECT query
    cursor = conn.cursor()
    cursor.execute(query, (role))
    results = cursor.fetchall()

    try:
        #store results in the return vals
        for row in results:
            commands.append(row[0])
    except Exception as e:
        if debug:
            print(e, file=sys.stderr)

    if debug:
        print("SQL is: " + query.format(command), file=sys.stderr)
        print(retrivedCommand, file=sys.stderr)
        print(response, file=sys.stderr)
        print(neededRole, file=sys.stderr)


    return commands

def delete(command):
    #Load globals needed
    global conn
    #make sure we have a connection to DB
    if conn == None:
        connect()
    #Make the SQL statement
    remove = "DELETE FROM commands WHERE command=%s"
    #Create cursor to execute query
    cursor = conn.cursor()
    #try the insert, rollback if error
    try:
        cursor.execute(remove, (command))
        conn.commit()
        return True
    except Exception as e:
        if debug:
            print(e, file=sys.stderr)
        conn.rollback()
        return False

#Returns bool of if roleHad is higher than or equal to roleNeeded
def hasAccess(roleHad, roleNeeded):
    #check if equal or if highest role
    if(roleHad == roleNeeded or roleHad == "Caster"):
        return True
    #check the other roles that they are above the needed
    else:
        if roleHad == "Mod" and roleNeeded != "Caster":
            return True
        elif roleHad == "Sub" and roleNeeded != "Caster" and roleNeeded != "Mod":
            return True
        elif roleHad == "Follower" and roleNeeded != "Caster" and roleNeeded != "Mod" and roleNeeded != "Sub":
            return True
        elif roleNeeded =="Normal":
            return True
        else:
            return False

def store(command,message,role): #TODO sanitize the inputs and add escapes and change backslash to forward if needed
    #Load globals needed
    global conn, roles
    if(command[0] != "!" or not role in roles):
        return False
    #make sure we have a connection to DB
    if conn == None:
        connect()
    #Make the SQL statement
    update = "INSERT INTO commands(command, role, response) VALUES(%s,%s,%s)"

    #Create cursor to execute query
    cursor = conn.cursor()
    #try the insert, rollback if error
    try:
        cursor.execute(update, (command, role, message))
        conn.commit()
        return True
    except Exception as e:
        if debug:
            print(e, file=sys.stderr)
        conn.rollback()
        return False

#gets a connection to the DB and stores it globally
def connect():
    global dbAddr, dbPass, dbUser, db, conn
    conn = pymysql.connect(dbAddr,dbUser,dbPass,db)

def main():
    try:
        loadConfig(sys.argv[1])
    except Exception as e:
        print("Invalid config file given")
        return -1
    toParse = read_in()
    action, user, response = parseCommand(toParse)
    #Close the connection before terminating thread
    if conn != None:
        conn.close()
    print(action + " " + user + " " + response)

#start process
if __name__ == '__main__':
    main()
