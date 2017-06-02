#Command handling module -  used for call-response type commands and interfacing with local data
# Returns info to the driver as a string in the form 'isValid user responseMsg'
# Expects info in form 'username highestRole messagetext'
import sys

#returns an array of the three inputs
#eg [username, role, message]
def read_in():
    lines = sys.stdin.readlines()
    return lines[0].split(maxsplit=2)

#returns the user and the response to the command
def parseCommand(input):
    user = input[0]
    role = input[1]
    message = input[2]
    response, neededRole = retrieve(message) #returns None, 'Root' if not in DB
    #TODO finish this method
    if(hasAccess(role,neededRole)):
        return response
    else:
        return None

def retrieve(message):
    response = None
    roleNeeded = 'Root'
    #TODO finish this method
    return response, neededRole

def hasAccess(roleHad, roleNeeded):
    if(roleHad == roleNeeded):
        return True
    else:
        return None #TODO actually implent

def main():
    toParse = read_in()
    idValid, user, response = parseCommand(toParse)
    print(isValid + " " + user + " " + response)

#start process
if __name__ == '__main__':
    main()
