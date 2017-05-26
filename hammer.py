# Moderation module, determines actions to take on individual messages
# Returns info to the driver as a string in the form 'action user responseMsg'
# Expects info in form 'username messagetext'
#TODO add regex and keyword detection
import sys, json
import profanityfilter

blacklist = []
debug = False

#Get the config data
def loadConfig():
    global blacklist
    with open('config.json') as data:
        config = json.load(data)
        blacklist = config["blacklist"]
        data.close()

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return lines[0].split(maxsplit=1)

#returns a "nothing", "timeout", "purge", or "ban"
def moderate(toParse):
    user = toParse[0]
    lines = toParse[1]
    actions = "nothing"
    responseMsg = ""
    banBool, banMsg = banCheck(lines)
    timeoutBool, timeoutMsg = timeoutCheck(lines)
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
    msg = "You have been banned for"
    profanityfilter.define_words(blacklist)
    if debug:
        print("Blacklist is:")
        print(blacklist)
        print("Filter is using these words:")
        print(profanityfilter.get_bad_words())
    if(profanityfilter.is_profane(message)):
        result = True
        msg += " blacklisted content"
    profanityfilter.restore_words()
    return result, msg

def timeoutCheck(message):
    result = False
    msg = "You have been timed-out for"
    #TODO replace with real code
    if(message.find("spam") != -1):
        result = True
        msg += " spam"
    return result, msg

def purgeCheck(message):
    result = False
    msg = "You have been purged"
    #TODO replace with real code
    if(message.find("annoy") != -1):
        result = True
    return result, msg

def main():
    loadConfig()

    #get our data as an array from read_in()
    toParse = read_in()

    actions, user, response = moderate(toParse)

    #return to the output stream
    print(actions + " " + user + " " + response)

#start process
if __name__ == '__main__':
    main()
