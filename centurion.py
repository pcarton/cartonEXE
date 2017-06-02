# Command handling module -  used for call-response type commands and interfacing with local data
# Returns info to the driver as a string in the form 'action user responseMsg'
# valid actions: ban timeout purge unban respond
# Expects info in form 'username highestRole messagetext'
# Valid roles for module ( may need to be altered by main service interface)
# Caster Mod Sub Follower Normal (in descending order)
import sys
import PyMySQL

builtins = ["!add","!ban","!purge","!timeout","!unban","!remove"]
conn = None
dbAddr = ""
dbUser = ""
dbPass = ""
db = ""
debug = False

#Get the config data
def loadConfig():
    global dbAddr, dbPass, dbUser, db debug
    with open('config.json') as data:
        config = json.load(data)
        debug = config["debug"]
        dbAddr = config["databaseURL"]
        dbPass = config["databasePassword"]
        dbUser = config["databaseUser"]
        db = confi["databaseName"]
        data.close()

#returns an array of the three inputs
#eg [username, role, message]
def read_in():
    lines = sys.stdin.readlines()
    return lines[0].split(maxsplit=2)

#returns the user and the response to the command
def parseCommand(input):
    global builtins
    user = input[0]
    role = input[1]
    message = input[2]
    if message in builtins:
        #TODO handle builtins
    else:
        response, neededRole = retrieve(message) #returns None, 'Root' if not in DB
        if(hasAccess(role,neededRole)):
            return response
        else:
            return None

def retrieve(message):
    global conn
    response = None
    roleNeeded = 'Root'

    if debug:
        print("Command is :" + message)

    query = "SELECT command, role, response FROM commands WHERE command={}"

    if conn == None:
        connect()
    cursor = conn.cursor()
    cursor.execute(query.format(message))
    results = cursor.fetchone()

    response = results[3]
    neededRole = results[2]

    return response, neededRole

def hasAccess(roleHad, roleNeeded):
    if(roleHad == roleNeeded or roleHad == "Caster"):
        return True
    else:
        if roleHad == "Mod" and roleNeeded != "Caster":
            return True
        elif roleHad == "Sub" and roleNeeded != "Caster" and roleNeeded != "Mod":
            return True
        elif roleHad == "Follower" and roleNeeded != "Caster" and roleNeeded != "Mod" and roleNeeded != "Sub":
            return True
        else:
            return False

def store(command,message,role):
    global conn
    if conn == None:
        connect()
    update = "INSERT INTO commands(command, role, response) VALUES({0},{1},{2});"

    cursor = conn.cursor()
    try:
        cursor.execute(update.format(command, role, message))
        conn.commit()
    except:
        conn.rollback()

def connect():
    global dbAddr, dbPass, dbUser, db, conn
    conn = PyMySQL.connect(dbAddr,dbUser,dbPass,db)

def main():
    loadConfig()
    toParse = read_in()
    action, user, response = parseCommand(toParse)
    if conn != None:
        conn.close()
    print(action + " " + user + " " + response)

#start process
if __name__ == '__main__':
    main()
