import unittest
from subprocess import call

from PyMods import centurion

class centurionTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

#TESTS FOR ADDING A NEW COMMAND
    def testParseCommandAddCasterNew(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!add","!testCmdNew1 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","New command !testCmdNew1 successfully stored"])

    def testParseCommandAddModNew(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!add","!testCmdNew2 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","New command !testCmdNew2 successfully stored"])

    def testParseCommandAddSubNew(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!add","!testCmdNew3 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerNew(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!add","!testCmdNew4 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalNew(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!add","!testCmdNew5 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR ADDING A COMMAND THAT EXISTS
    def testParseCommandAddCasterExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Error storing new command in database"])

    def testParseCommandAddModExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Error storing new command in database"])

    def testParseCommandAddSubExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR ADDING COMMAND WITHOUT ARGS
    def testParseCommandAddCasterInvalid(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!add","!testCmdNew6"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddModInvalid(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!add","!testCmdNew7"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddSubInvalid(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!add","!testCmdNew8"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerInvalid(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!add","!testCmdNew9"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalInvalid(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!add","!testCmdNew10"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR ADDING COMMAND WITHOUT A ROLE
    def testParseCommandAddCasterInvalid2(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!add","!testCmdNew11 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddModInvalid2(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!add","!testCmdNew12 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddSubInvalid2(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!add","!testCmdNew13 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerInvalid2(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!add","!testCmdNew14 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalInvalid2(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!add","!testCmdNew15 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR !remove COMMAND
    def testParseCommandRemoveCasterExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!remove","!testRemoveExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Command !testRemoveExisting1 successfully removed"])

    def testParseCommandRemoveModExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!remove","!testRemoveExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Command !testRemoveExisting2 successfully removed"])

    def testParseCommandRemoveSubExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!remove","!testRemoveExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveFollowerExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!remove","!testRemoveExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveNormalExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!remove","!testRemoveExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR INVALID !remove COMMAND
    def testParseCommandRemoveCasterNotExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","That command does not exist"])

    def testParseCommandRemoveModNotExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","That command does not exist"])

    def testParseCommandRemoveSubNotExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveFollowerNotExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveNormalNotExisting(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

if __name__ == "__main__":
        unittest.main()
