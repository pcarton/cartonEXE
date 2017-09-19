# Logging Module
# Returns no info to driver
# Expects info in form 'action username highestRole messagetext'
# action can be: 'purge', 'timeout', 'ban', 'unban', 'chat'
import sys, pymysql, datetime, json

debug = False
fmt = '%Y-%m-%d %H:%M:%S'

logFile = ""
logExtension = ""

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    line = lines[0].strip()
    return line.split(maxsplit=3)

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

#start process
if __name__ == '__main__':
    main()
