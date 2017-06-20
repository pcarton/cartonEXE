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
fmt = '%Y-%m-%d %H:%M:%S'

#Get the config data
def loadConfig():
    global dbAddr, dbPass, dbUser, db, debug
    with open('config.json') as data:
        config = json.load(data)
        debug = config["debug"]
        dbAddr = config["databaseURL"]
        dbPass = config["databasePassword"]
        dbUser = config["databaseUser"]
        db = config["databaseName"]
        data.close()

#returns True if action success, False if exception encountered
def removePermits(username):
    loadConfig()
    if debug:
        print("Removing user " + username + "'s permits'")
    #Load globals needed
    global conn, debug
    #make sure we have a connection to DB
    if conn == None:
        connect()
    #Make the SQL statement
    remove = "DELETE FROM permits WHERE user='{}'"
    #Create cursor to execute query
    cursor = conn.cursor()
    #try the insert, rollback if error
    try:
        cursor.execute(remove.format(username))
        conn.commit()
        return True
    except Exception as e:
        if debug:
            print(e)
        conn.rollback()
        return False

def addPermits(username):
    loadConfig()
    #Load globals needed
    global conn, debug

    #make sure we have a connection to DB
    if conn == None:
        connect()

    #Make the SQL statement
    update = "INSERT INTO permits(user,expiration) VALUES('{0}','{1}')"

    #make the expiration object
    time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    timeStr = pythonToString(time)
    if debug:
        print("Adding new permit with following time to the database:")
        print(time)
        print(timeStr)

    #Create cursor to execute query
    cursor = conn.cursor()
    #try the insert, rollback if error
    try:
        cursor.execute(update.format(username, timeStr))
        conn.commit()
        return True
    except Exception as e:
        if debug:
            print(e)
        conn.rollback()
        return False

#returns the expiration date of the user's permit, or None if no permit exists
def getPermit(username):
    loadConfig()
    if debug:
        print("Querying Database for permit")
    #Load globals needed
    global conn, debug

    #prepare default return values
    expir = None

    #make the SQL statement
    query = "SELECT expiration FROM permits WHERE user='{}'"
    #make sure we have a connection to the DB
    if conn == None:
        connect()
    #create a cursor to execute SELECT query
    cursor = conn.cursor()
    cursor.execute(query.format(username))
    results = cursor.fetchone()

    try:
        #store results in the return vals
        expir = results[0]
    except Exception as e:
        if debug:
            print(e)

    return expir

def isPermitted(username):
    loadConfig()
    if debug:
        print("Checking that user " + username + " is permitted")
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
    return lines[0]

def main():
    loadConfig()
    #get our data as an array from read_in()
    username= read_in()
    actions = "nothing"
    msg = ""

    if isPermitted(username):
        removePermits(username)
    else:
        msg = "Please ask for permission before posting links"
        actions = "timeout"

    #return to the output stream
    print(actions + " " + username + " " + msg)

#start process
if __name__ == '__main__':
    main()
