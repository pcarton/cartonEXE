#Link handling module - used for permits and such
# Returns info to the driver as a string in the form 'action user responseMsg'
# Expects info in form 'username highestRole messagetext'
import sys, pymysql, datetime, json

conn = None
dbAddr = ""
dbUser = ""
dbPass = ""
db = ""
debug = False
whitelisted = []
fmt = '%Y-%m-%d %H:%M:%S'

CONFIG_PATH = sys.argv[1]

#Get the config data
def loadConfig(configPath):
    global dbAddr, dbPass, dbUser, db, debug, whitelisted, CONFIG_PATH
    CONFIG_PATH = configPath
    with open(configPath) as data:
        config = json.load(data)
        debug = config["debug"]
        dbAddr = config["databaseURL"]
        dbPass = config["databasePassword"]
        dbUser = config["databaseUser"]
        db = config["databaseName"]
        whitelisted = config["linkPosterWhitelist"]
        data.close()

#returns True if action success, False if exception encountered
def removePermits(username):
    #Load globals needed
    global conn, debug
    loadConfig(CONFIG_PATH)
    if debug:
        print("Removing user " + username + "'s permits", file=sys.stderr)
    #make sure we have a connection to DB
    if conn == None:
        connect()
    #Treat the name not in database same as an error
    if getPermit(username)==None:
        return False
    #Make the SQL statement
    remove = "DELETE FROM permits WHERE user=%s"
    #Create cursor to execute query
    cursor = conn.cursor()
    #try the insert, rollback if error
    try:
        cursor.execute(remove, (username))
        conn.commit()
        return True
    except Exception as e:
        if debug:
            print(e)
        conn.rollback()
        return False

def addPermits(username):
    loadConfig(CONFIG_PATH)
    #Load globals needed
    global conn, debug

    #make sure we have a connection to DB
    if conn == None:
        connect()

    #Make the SQL statement
    insert = "INSERT INTO permits(user,expiration) VALUES(%s,%s)"
    update = "UPDATE permits SET expiration = %s WHERE user = %s"

    #make the expiration object
    time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    timeStr = pythonToString(time)
    if debug:
        print("Adding new permit with following time to the database:", file=sys.stderr)
        print(time ,file=sys.stderr)
        print(timeStr, file=sys.stderr)

    #Create cursor to execute query
    cursor = conn.cursor()
    #try the insert, rollback if error

    if getPermit(username) != None:
        try:
            cursor.execute(update, (username, timeStr))
            conn.commit()
            return True
        except Excetion as e:
            if debug:
                print(e)
            conn.rollback()
            return False
    else:
        try:
            cursor.execute(insert, (username, timeStr))
            conn.commit()
            return True
        except Exception as e:
            if debug:
                print(e)
            conn.rollback()
            return False

#returns the expiration date of the user's permit, or None if no permit exists
def getPermit(username):
    #Load globals needed
    global conn, debug
    loadConfig(CONFIG_PATH)
    if debug:
        print("Querying Database for permit", file=sys.stderr)

    #prepare default return values
    expir = None

    #make the SQL statement
    query = "SELECT expiration FROM permits WHERE user=%s"
    #make sure we have a connection to the DB
    if conn == None:
        connect()
    #create a cursor to execute SELECT query
    cursor = conn.cursor()
    cursor.execute(query, (username))
    results = cursor.fetchone()

    if results != None:
        try:
            #store results in the return vals
            expir = results[0]
        except Exception as e:
            if debug:
                print(e, file=sys.stderr)

    return expir

def isPermitted(username):
    global debug, whitelisted
    loadConfig(CONFIG_PATH)
    if debug:
        print("Checking that user " + username + " is permitted", file=sys.stderr)
        print("Whitelisted users are:", file=sys.stderr)
        print(whitelisted, file=sys.stderr)
    if username in whitelisted:
        return True
    expir = getPermit(username)
    if expir == None:
        return False
    hasntExpired = expir > datetime.datetime.utcnow()
    return hasntExpired

#converts string to python datetime
def stringToPython(timestamp):
    global fmt #global formating string
    datetimeObj = datetime.datetime.strptime(timestamp,fmt)
    return datetimeObj

#converts python datetime to string
def pythonToString(datetimeObj):
    global fmt #global formating string
    return datetimeObj.strftime(fmt)


#gets a connection to the DB and stores it globally
def connect():
    global dbAddr, dbPass, dbUser, db, conn
    conn = pymysql.connect(dbAddr,dbUser,dbPass,db)

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    line = lines[0].strip()
    return line.split(maxsplit=1)

def main():
    global debug
    loadConfig(CONFIG_PATH)
    #get our data as an array from read_in()
    lines = read_in()
    username = lines[0]
    role = lines[1]
    actions = "nothing"
    msg = ""
    if debug:
        print("Username:" + username, file=sys.stderr)
        print("Role:" + role, file=sys.stderr)

    if isPermitted(username):
        removePermits(username)
    elif not (role == "Mod" or role == "Caster"):
        msg = "Please ask for permission before posting links"
        actions = "timeout"

    #return to the output stream
    print(actions + " " + username + " " + msg)

#start process
if __name__ == '__main__':
    main()
