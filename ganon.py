#Link handling module - used for permits and such
# Returns info to the driver as a string in the form 'action user responseMsg'
# Expects info in form 'username highestRole messagetext'
import sys,pymysql

conn = None
dbAddr = ""
dbUser = ""
dbPass = ""
db = ""
debug = False

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
def removePermit(username):
    #Load globals needed
    global conn
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

def addPermit(username): #TODO

#returns the expiration date of the user's permit, or None if no permit exists
def getPermit(username):
    #Load globals needed
    global conn

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
        expir = results[0] #TODO turn into datetime obj
    except Exception as e:
        if debug:
            print(e)

    return expir

def isPermitted(username):
    return not getPermit(username) == None

#converts string to python datetime
def stringToPython(string):

#converts python datetime to string
def pythonToString(datetimeObj):
    

#gets a connection to the DB and stores it globally
def connect():
    global dbAddr, dbPass, dbUser, db, conn
    conn = pymysql.connect(dbAddr,dbUser,dbPass,db)

def main():
    loadConfig()
    #TODO add the logic/input parsing
    #Close the connection before terminating thread
    if conn != None:
        conn.close()
    #TODO add the output

#start process
if __name__ == '__main__':
    main()
