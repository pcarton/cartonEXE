import unittest
from subprocess import call

import centurion

class centurionTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

#TESTS FOR IF THE CONFIG LOADED CORRECTLY
    def testLoadConfigAddr(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbAddr, "localhost")

    def testLoadConfigPass(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbPass, "root")

    def testLoadConfigUser(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbUser, "root")

    def testLoadConfigName(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.db, "cartonBotTest")

    def testLoadConfigDebug(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.debug, False)

#TESTS FOR IF A CASTER HAS ACCESS
    def testHasAccessCasterCaster(self):
        roleHad = "Caster"
        roleNeeded = "Caster"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessCasterMod(self):
        roleHad = "Caster"
        roleNeeded = "Mod"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessCasterSub(self):
        roleHad = "Caster"
        roleNeeded = "Sub"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessCasterFollower(self):
        roleHad = "Caster"
        roleNeeded = "Follower"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessCasterNormal(self):
        roleHad = "Caster"
        roleNeeded = "Normal"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

#TESTS FOR IF A MOD HAS ACCESS
    def testHasAccessModCaster(self):
        roleHad = "Mod"
        roleNeeded = "Caster"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessModMod(self):
        roleHad = "Mod"
        roleNeeded = "Mod"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessModSub(self):
        roleHad = "Mod"
        roleNeeded = "Sub"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessModFollower(self):
        roleHad = "Mod"
        roleNeeded = "Follower"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessModNormal(self):
        roleHad = "Mod"
        roleNeeded = "Normal"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

#TESTS FOR IF A SUB HAS ACCESS
    def testHasAccessSubCaster(self):
        roleHad = "Sub"
        roleNeeded = "Caster"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessSubMod(self):
        roleHad = "Sub"
        roleNeeded = "Mod"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessSubSub(self):
        roleHad = "Sub"
        roleNeeded = "Sub"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessSubFollower(self):
        roleHad = "Sub"
        roleNeeded = "Follower"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessSubNormal(self):
        roleHad = "Sub"
        roleNeeded = "Normal"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

#TESTS FOR IF A FOLLOWER HAS ACCESS
    def testHasAccessFollowerCaster(self):
        roleHad = "Follower"
        roleNeeded = "Caster"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessFollowerMod(self):
        roleHad = "Follower"
        roleNeeded = "Mod"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessFollowerSub(self):
        roleHad = "Follower"
        roleNeeded = "Sub"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessFollowerFollower(self):
        roleHad = "Follower"
        roleNeeded = "Follower"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

    def testHasAccessFollowerNormal(self):
        roleHad = "Follower"
        roleNeeded = "Normal"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

#TESTS FOR IF A NORMAL USER HAS ACCESS
    def testHasAccessNormalCaster(self):
        roleHad = "Normal"
        roleNeeded = "Caster"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalMod(self):
        roleHad = "Normal"
        roleNeeded = "Mod"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalSub(self):
        roleHad = "Normal"
        roleNeeded = "Sub"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalFollower(self):
        roleHad = "Normal"
        roleNeeded = "Follower"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalNormal(self):
        roleHad = "Normal"
        roleNeeded = "Normal"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

#TESTS FOR ADDING A NEW COMMAND
    def testParseCommandAddCasterNew(self):
        inputList = ["PCarton","Caster","!add","!testCmdNew1 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","New command !testCmdNew1 successfully stored"])

    def testParseCommandAddModNew(self):
        inputList = ["PCarton","Mod","!add","!testCmdNew2 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","New command !testCmdNew2 successfully stored"])

    def testParseCommandAddSubNew(self):
        inputList = ["PCarton","Sub","!add","!testCmdNew3 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerNew(self):
        inputList = ["PCarton","Follower","!add","!testCmdNew4 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalNew(self):
        inputList = ["PCarton","Normal","!add","!testCmdNew5 Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR ADDING A COMMAND THAT EXISTS
    def testParseCommandAddCasterExisting(self):
        inputList = ["PCarton","Caster","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Error storing new command in database"])

    def testParseCommandAddModExisting(self):
        inputList = ["PCarton","Mod","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Error storing new command in database"])

    def testParseCommandAddSubExisting(self):
        inputList = ["PCarton","Sub","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerExisting(self):
        inputList = ["PCarton","Follower","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalExisting(self):
        inputList = ["PCarton","Normal","!add","!testCmdExisting Mod blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR ADDING COMMAND WITHOUT ARGS
    def testParseCommandAddCasterInvalid(self):
        inputList = ["PCarton","Caster","!add","!testCmdNew6"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddModInvalid(self):
        inputList = ["PCarton","Mod","!add","!testCmdNew7"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddSubInvalid(self):
        inputList = ["PCarton","Sub","!add","!testCmdNew8"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerInvalid(self):
        inputList = ["PCarton","Follower","!add","!testCmdNew9"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalInvalid(self):
        inputList = ["PCarton","Normal","!add","!testCmdNew10"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR ADDING COMMAND WITHOUT A ROLE
    def testParseCommandAddCasterInvalid2(self):
        inputList = ["PCarton","Caster","!add","!testCmdNew11 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddModInvalid2(self):
        inputList = ["PCarton","Mod","!add","!testCmdNew12 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Invalid new command. Expected Format: '!newCmd requiredRole response'"])

    def testParseCommandAddSubInvalid2(self):
        inputList = ["PCarton","Sub","!add","!testCmdNew13 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddFollowerInvalid2(self):
        inputList = ["PCarton","Follower","!add","!testCmdNew14 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandAddNormalInvalid2(self):
        inputList = ["PCarton","Normal","!add","!testCmdNew15 blah blah blah"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR !remove COMMAND
    def testParseCommandRemoveCasterExisting(self):
        inputList = ["PCarton","Caster","!remove","!testRemoveExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Command !testRemoveExisting1 successfully removed"])

    def testParseCommandRemoveModExisting(self):
        inputList = ["PCarton","Mod","!remove","!testRemoveExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","Command !testRemoveExisting2 successfully removed"])

    def testParseCommandRemoveSubExisting(self):
        inputList = ["PCarton","Sub","!remove","!testRemoveExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveFollowerExisting(self):
        inputList = ["PCarton","Follower","!remove","!testRemoveExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveNormalExisting(self):
        inputList = ["PCarton","Normal","!remove","!testRemoveExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR INVALID !remove COMMAND
    def testParseCommandRemoveCasterNotExisting(self):
        inputList = ["PCarton","Caster","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","That command does not exist"])

    def testParseCommandRemoveModNotExisting(self):
        inputList = ["PCarton","Mod","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","That command does not exist"])

    def testParseCommandRemoveSubNotExisting(self):
        inputList = ["PCarton","Sub","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveFollowerNotExisting(self):
        inputList = ["PCarton","Follower","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testParseCommandRemoveNormalNotExisting(self):
        inputList = ["PCarton","Normal","!remove","!testRemoveInvalid"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR PURGE COMMAND
    def testParseCommandPurgeCaster(self):
        inputList = ["PCarton","Caster","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["purge","Garlian","Purging user: Garlian"])

    def testParseCommandPurgeMod(self):
        inputList = ["PCarton","Mod","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["purge","Garlian","Purging user: Garlian"])

    def testParseCommandPurgeSub(self):
        inputList = ["PCarton","Sub","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeFollower(self):
        inputList = ["PCarton","Follower","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeNormal(self):
        inputList = ["PCarton","Normal","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID PURGE COMMAND
    def testParseCommandPurgeCasterNoArgs(self):
        inputList = ["PCarton","Caster","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeModNoArgs(self):
        inputList = ["PCarton","Mod","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeSubNoArgs(self):
        inputList = ["PCarton","Sub","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeFollowerNoArgs(self):
        inputList = ["PCarton","Follower","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeNormalNoArgs(self):
        inputList = ["PCarton","Normal","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID PURGE COMMAND 2
    def testParseCommandPurgeCasterBadArgs(self):
        inputList = ["PCarton","Caster","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeModBadArgs(self):
        inputList = ["PCarton","Mod","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeSubBadArgs(self):
        inputList = ["PCarton","Sub","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeFollowerBadArgs(self):
        inputList = ["PCarton","Follower","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeNormalBadArgs(self):
        inputList = ["PCarton","Normal","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR TIMEOUT COMMAND
    def testParseCommandTimeoutCaster(self):
        inputList = ["PCarton","Caster","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["timeout","Garlian","Timing out user: Garlian"])

    def testParseCommandTimeoutMod(self):
        inputList = ["PCarton","Mod","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["timeout","Garlian","Timing out user: Garlian"])

    def testParseCommandTimeoutSub(self):
        inputList = ["PCarton","Sub","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutFollower(self):
        inputList = ["PCarton","Follower","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutNormal(self):
        inputList = ["PCarton","Normal","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID TIMEOUT COMMAND
    def testParseCommandTimeoutCasterNoArgs(self):
        inputList = ["PCarton","Caster","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutModNoArgs(self):
        inputList = ["PCarton","Mod","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutSubNoArgs(self):
        inputList = ["PCarton","Sub","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutFollowerNoArgs(self):
        inputList = ["PCarton","Follower","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutNormalNoArgs(self):
        inputList = ["PCarton","Normal","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID TIMEOUT COMMAND 2
    def testParseCommandTimeoutCasterBadArgs(self):
        inputList = ["PCarton","Caster","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutModBadArgs(self):
        inputList = ["PCarton","Mod","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutSubBadArgs(self):
        inputList = ["PCarton","Sub","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutFollowerBadArgs(self):
        inputList = ["PCarton","Follower","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutNormalBadArgs(self):
        inputList = ["PCarton","Normal","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR BAN COMMAND
    def testParseCommandbanCaster(self):
        inputList = ["PCarton","Caster","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["ban","Garlian","Banning user: Garlian"])

    def testParseCommandbanMod(self):
        inputList = ["PCarton","Mod","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["ban","Garlian","Banning user: Garlian"])

    def testParseCommandbanSub(self):
        inputList = ["PCarton","Sub","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandbanFollower(self):
        inputList = ["PCarton","Follower","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandbanNormal(self):
        inputList = ["PCarton","Normal","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID BAN COMMAND
    def testParseCommandbanCasterNoArgs(self):
        inputList = ["PCarton","Caster","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandbanModNoArgs(self):
        inputList = ["PCarton","Mod","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandbanSubNoArgs(self):
        inputList = ["PCarton","Sub","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandbanFollowerNoArgs(self):
        inputList = ["PCarton","Follower","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandbanNormalNoArgs(self):
        inputList = ["PCarton","Normal","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID BAN COMMAND 2
    def testParseCommandbanCasterBadArgs(self):
        inputList = ["PCarton","Caster","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandbanModBadArgs(self):
        inputList = ["PCarton","Mod","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandbanSubBadArgs(self):
        inputList = ["PCarton","Sub","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandbanFollowerBadArgs(self):
        inputList = ["PCarton","Follower","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandbanNormalBadArgs(self):
        inputList = ["PCarton","Normal","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

if __name__ == "__main__":
        unittest.main()
