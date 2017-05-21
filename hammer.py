# Moderation module, determines actions to take on individual messages
import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines)

#returns a "nothing", "timeout", "purge", or "ban"
def moderate(lines):
    actions = "nothing"

    return actions

def main():
    #get our data as an array from read_in()
    lines = read_in()

    actions = moderate(lines);

    #return the sum to the output stream
    print(actions)

#start process
if __name__ == '__main__':
    main()
