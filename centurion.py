# Command handling module -  used for call-response type commands and interfacing with local data
# Returns info to the driver as a string in the form 'action user responseMsg'
# valid actions: ban timeout purge unban respond
# Expects info in form 'username highestRole messagetext'
import sys
import PyMySQL

builtins = []
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
        #TODO finish this method
        if(hasAccess(role,neededRole)):
            return response
        else:
            return None

def retrieve(message):
    global conn
    response = None
    roleNeeded = 'Root'
    if conn == None:
        connect()
    else:
        #TODO store the new command
    return response, neededRole

def hasAccess(roleHad, roleNeeded):
    if(roleHad == roleNeeded):
        return True
    else:
        return None #TODO actually implent

def store(command,message,role):
    global conn
    if conn == None:
        connect()
    else:
        #TODO store the new command

def connect():
    global dbAddr, dbPass, dbUser, db, conn
    conn = PyMySQL.connect(dbAddr,)

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
