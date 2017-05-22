# Moderation module, determines actions to take on individual messages
# Returns info to the driver as a string in the form 'action user responseMsg'
# Expects info in form 'username messagetext'
#TODO add regex and keyword detection
import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return lines[0].split(maxsplit=1)

#returns a "nothing", "timeout", "purge", or "ban"
def moderate(toParse):
    user = toParse[1]
    lines = toParse[0]
    actions = "nothing"
    responseMsg = ""
    if lines.find("blacklist") != -1:
        actions = "ban"
        responseMsg = "You have been banned for Blacklisted content"
    elif lines.find("spam") != -1:
        actions = "timeout";
        responseMsg = "You have been timed out for spam"
    elif lines.find("annoy") != -1:
        actions = "purge"
        responseMsg = "You have been purged"
    return actions, user, responseMsg

def main():
    #get our data as an array from read_in()
    toParse = read_in()

    actions, user, response = moderate(toParse)

    #return to the output stream
    print(actions + " " + user + " " + response)

#start process
if __name__ == '__main__':
    main()
