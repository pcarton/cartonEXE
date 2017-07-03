import unittest
import centurion

class centurionTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

    def testLoadConfig(self):
        centurion.loadConfig(self.CONFIG_PATH)
        configList = ["DBAddrTEST","DBPassTEST","DBUserTEST","DBNameTEST",False]
        resultList = [centurion.dbAddr, centurion.dbPass, centurion.dbUser, centurion.db, centurion.debug,]
        self.assertEqual(resultList, configList)

    def testLoadConfigAddr(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbAddr, "DBAddrTEST")

    def testLoadConfigPass(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbPass, "DBPassTEST")

    def testLoadConfigUser(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbUser, "DBUserTEST")

    def testLoadConfigName(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.db, "DBNameTEST")

    def testLoadConfigDebug(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.debug, False)

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

    def testHasAccessNormalCaster(self):
        roleHad = "Caster"
        roleNeeded = "Caster"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalMod(self):
        roleHad = "Caster"
        roleNeeded = "Mod"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalSub(self):
        roleHad = "Caster"
        roleNeeded = "Sub"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalFollower(self):
        roleHad = "Caster"
        roleNeeded = "Follower"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),False)

    def testHasAccessNormalNormal(self):
        roleHad = "Caster"
        roleNeeded = "Normal"
        self.assertEqual(centurion.hasAccess(roleHad,roleNeeded),True)

if __name__ == "__main__":
            unittest.main()
