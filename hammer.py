import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines)

def moderate(lines):
    actions = "" # empty string if no action to take

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
