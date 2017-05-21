# Moderation module, determines actions to take on individual messages
#TODO add moderator/brodcaster checks
#TODO add regex and keyword detection
import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return lines[0]

#returns a "nothing", "timeout", "purge", or "ban"
def moderate(lines):
    actions = "nothing"
    responseMsg = ""
    if lines.find("blacklist") != -1:
        actions = "ban"
        responseMsg = "you have been banned for Blacklisted content"
    elif lines.find("spam") != -1:
        actions = "timeout";
        responseMsg = "You have been timed out for spam"
    elif lines.find("annoy") != -1:
        actions = "purge"
        responseMsg = "You have been purged"
    return actions, responseMsg

def main():
    #get our data as an array from read_in()
    lines = read_in()

    actions, response = moderate(lines)

    #return to the output stream
    print(actions + " " + response)

#start process
if __name__ == '__main__':
    main()
