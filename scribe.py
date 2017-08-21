# Logging Module
# Returns no info to driver
# Expects info in form 'action username highestRole messagetext'
import sys, pymysql, datetime, json

debug = False
fmt = '%Y-%m-%d %H:%M:%S'

logFile = ""
logExtension = ""

CONFIG_PATH = 'config.json'

#Get the config data
def loadConfig(configPath):
    global logFile, logExtension, debug, CONFIG_PATH
    CONFIG_PATH = configPath
    with open(configPath) as data:
        config = json.load(data)
        debug = config["debug"]
        logFile = config["logFile"]
        logExtension = config["logExtension"]
        data.close()
