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

def removePermit(username):

def addPermit(username):

def getPermit(username):

def isPermitted(username):
    return not getPermit(username) == None
