# Moderation module, determines actions to take on individual messages
# Returns info to the driver as a string in the form 'action user responseMsg'
# Expects info in form 'username messagetext'
import sys, json, re
import profanityfilter
import ganon

linkCheck = "(https?:\/\/)?([\da-z\.]+)\.([a-z\.]{2,6})([/\w\.-]*)*\/?"
linkRegEx = re.compile(linkCheck)

blacklist = []
debug = False

#Get the config data
def loadConfig(configPath):
    global blacklist, debug, CONFIG_PATH
    CONFIG_PATH = configPath
    with open(configPath) as data:
        config = json.load(data)
        blacklist = config["blacklist"]
        debug = config["debug"]
        data.close()
    ganon.loadConfig(CONFIG_PATH)

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return lines[0].split(maxsplit=2)

#returns a "nothing", "timeout", "purge", or "ban"
def moderate(toParse):
    user = toParse[0]
    role = toParse[1]
    lines = toParse[2]
    actions = "nothing"
    responseMsg = ""
    banBool, banMsg = banCheck(lines)
    timeoutBool, timeoutMsg = timeoutCheck(user,lines)
    purgeBool, purgeMsg = purgeCheck(lines)
    if banBool:
        actions = "ban"
        responseMsg = banMsg
    elif timeoutBool:
        actions = "timeout";
        responseMsg = timeoutMsg
    elif purgeBool:
        actions = "purge"
        responseMsg = purgeMsg
    return actions, user, responseMsg

def banCheck(message):
    result = False
    msg = "You have been banned for "
    if blacklist:
        profanityfilter.define_words(blacklist)
        if debug:
            print("Blacklist is:", file=sys.stderr)
            print(blacklist, file=sys.stderr)
            print("Filter is using these words:", file=sys.stderr)
            print(profanityfilter.get_bad_words(), file=sys.stderr)
        if(profanityfilter.is_profane(message)):
            result = True
            msg += "blacklisted content"
        profanityfilter.restore_words()
    else:
        msg = ""
    return result, msg

def timeoutCheck(username, message):
    result = False
    msg = "You have been timed-out for "
    #TODO replace with real code
    if message.find("spam") != -1 :
        result = True
        msg += "spam"
    else:
        msg = ""
    return result, msg
    return False, ""

def purgeCheck(message):
    result = False
    msg = "You have been purged"
    #TODO replace with real code
    if message.find("annoy") != -1 :
        result = True
    #return result, msg
    return False, ""

def main():
    try:
        loadConfig(sys.argv[1])
    except Exception as e:
        print("Invalid config file given")
        return -1

    #get our data as an array from read_in()
    toParse = read_in()

    actions, user, response = moderate(toParse)

    #return to the output stream
    print(actions + " " + user + " " + response)

#start process
if __name__ == '__main__':
    main()
