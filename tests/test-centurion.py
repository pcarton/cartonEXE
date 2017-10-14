import unittest
from subprocess import call

from modules import centurion

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

#TESTS FOR PURGE COMMAND
    def testParseCommandPurgeCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["purge","Garlian","Purging user: Garlian"])

    def testParseCommandPurgeMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["purge","Garlian","Purging user: Garlian"])

    def testParseCommandPurgeSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!purge","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID PURGE COMMAND
    def testParseCommandPurgeCasterNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeModNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeSubNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeFollowerNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeNormalNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!purge",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID PURGE COMMAND 2
    def testParseCommandPurgeCasterBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeModBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPurgeSubBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeFollowerBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPurgeNormalBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!purge","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR TIMEOUT COMMAND
    def testParseCommandTimeoutCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["timeout","Garlian","Timing out user: Garlian"])

    def testParseCommandTimeoutMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["timeout","Garlian","Timing out user: Garlian"])

    def testParseCommandTimeoutSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!timeout","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID TIMEOUT COMMAND
    def testParseCommandTimeoutCasterNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutModNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutSubNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutFollowerNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutNormalNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!timeout",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID TIMEOUT COMMAND 2
    def testParseCommandTimeoutCasterBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutModBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandTimeoutSubBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutFollowerBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandTimeoutNormalBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!timeout","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR BAN COMMAND
    def testParseCommandBanCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["ban","Garlian","Banning user: Garlian"])

    def testParseCommandBanMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["ban","Garlian","Banning user: Garlian"])

    def testParseCommandBanSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandBanFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandBanNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!ban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID BAN COMMAND
    def testParseCommandBanCasterNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandBanModNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandBanSubNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandBanFollowerNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandBanNormalNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!ban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID BAN COMMAND 2
    def testParseCommandBanCasterBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandBanModBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandBanSubBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandBanFollowerBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandBanNormalBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!ban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR unban COMMAND
    def testParseCommandUnbanCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!unban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["unban","Garlian","Unbanning user: Garlian"])

    def testParseCommandUnbanMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!unban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["unban","Garlian","Unbanning user: Garlian"])

    def testParseCommandUnbanSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!unban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandUnbanFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!unban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandUnbanNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!unban","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID unban COMMAND
    def testParseCommandUnbanCasterNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!unban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandUnbanModNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!unban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandUnbanSubNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!unban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandUnbanFollowerNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!unban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandUnbanNormalNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!unban",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID unban COMMAND 2
    def testParseCommandUnbanCasterBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!unban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandUnbanModBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!unban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandUnbanSubBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!unban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandUnbanFollowerBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!unban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandUnbanNormalBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!unban","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR PERMIT COMMAND
    def testParseCommandPermitCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!permit","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","Garlian","User Garlian is allowed to post 1 link in the next 10 minutes"])

    def testParseCommandPermitMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!permit","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","Garlian","User Garlian is allowed to post 1 link in the next 10 minutes"])

    def testParseCommandPermitSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!permit","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPermitFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!permit","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPermitNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!permit","Garlian"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID PERMIT COMMAND
    def testParseCommandPermitCasterNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!permit",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPermitModNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!permit",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPermitSubNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!permit",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPermitFollowerNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!permit",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPermitNormalNoArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!permit",""]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR INVALID PERMIT COMMAND 2
    def testParseCommandPermitCasterBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!permit","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPermitModBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!permit","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Invalid Args"])

    def testParseCommandPermitSubBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!permit","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPermitFollowerBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!permit","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandPermitNormalBadArgs(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!permit","Garlian is silly"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR DEATHBLOSSOM COMMAND
    def testParseCommandDeathBlossomCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!deathblossom"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["deathblossom","PCarton","Toggled deathblossom mode"])

    def testParseCommandDeathBlossomMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!deathblossom"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["deathblossom","PCarton","Toggled deathblossom mode"])

    def testParseCommandDeathBlossomSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!deathblossom"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandDeathBlossomFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!deathblossom"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

    def testParseCommandDeathBlossomNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!deathblossom"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton","Required Role not met"])

#TESTS FOR USING CASTER COMMAND IN DATABASE
    def testAsCasterDBCommandCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!testExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF ONE"])

    def testAsModDBCommandCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!testExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testAsSubDBCommandCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!testExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testAsFollowerDBCommandCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!testExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testAsNormalDBCommandCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!testExisting1"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR USING MOD COMMAND IN DATABASE
    def testAsCasterDBCommandMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!testExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF TWO"])

    def testAsModDBCommandMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!testExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF TWO"])

    def testAsSubDBCommandMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!testExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testAsFollowerDBCommandMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!testExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testAsNormalDBCommandMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!testExisting2"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR USING SUB COMMAND IN DATABASE
    def testAsCasterDBCommandSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!testExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF THREE"])

    def testAsModDBCommandSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!testExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF THREE"])

    def testAsSubDBCommandSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!testExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF THREE"])

    def testAsFollowerDBCommandSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!testExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

    def testAsNormalDBCommandSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!testExisting3"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR USING FOLLOWER COMMAND IN DATABASE
    def testAsCasterDBCommandFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!testExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FOUR"])

    def testAsModDBCommandFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!testExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FOUR"])

    def testAsSubDBCommandFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!testExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FOUR"])

    def testAsFollowerDBCommandFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!testExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FOUR"])

    def testAsNormalDBCommandFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!testExisting4"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["none","PCarton",""])

#TESTS FOR USING NORMAL COMMAND IN DATABASE
    def testAsCasterDBCommandNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Caster","!testExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FIVE"])

    def testAsModDBCommandNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Mod","!testExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FIVE"])

    def testAsSubDBCommandNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Sub","!testExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FIVE"])

    def testAsFollowerDBCommandNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Follower","!testExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FIVE"])

    def testAsNormalDBCommandNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["PCarton","Normal","!testExisting5"]
        action, user, response = centurion.parseCommand(inputList)
        self.assertEqual([action, user, response],["respond","PCarton","TEST FOR EXISTING COMMAND STUFF FIVE"])

#TESTS FOR RETRIEVING A LIST OF COMMANDS
    def testRetrievListCaster(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["Caster"]
        commands = centurion.retrieveList(inputList)
        self.assertEqual(commands,["!testRemoveExisting1","!testExisting1"])
    def testRetrievListMod(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["Mod"]
        commands = centurion.retrieveList(inputList)
        self.assertEqual(commands,["!testCmdExisting","!testRemoveExisting2","!testExisting2"])
    def testRetrievListSub(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["Sub"]
        commands = centurion.retrieveList(inputList)
        self.assertEqual(commands,["!testRemoveExisting3","!testExisting3"])
    def testRetrievListFollower(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["Follower"]
        commands = centurion.retrieveList(inputList)
        self.assertEqual(commands,["!testRemoveExisting4","!testExisting4"])
    def testRetrievListNormal(self):
        centurion.loadConfig(self.CONFIG_PATH)
        inputList = ["Normal"]
        commands = centurion.retrieveList(inputList)
        self.assertEqual(commands,["!testRemoveExisting5","!testExisting5"])

if __name__ == "__main__":
        unittest.main()
