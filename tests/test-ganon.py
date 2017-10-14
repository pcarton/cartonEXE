import unittest
from subprocess import call
import datetime

import modules.ganon

class ganonTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

#TESTS FOR IF THE CONFIG LOADED CORRECTLY
    def testLoadConfigAddr(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.dbAddr, "localhost")

    def testLoadConfigPass(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.dbPass, "root")

    def testLoadConfigUser(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.dbUser, "root")

    def testLoadConfigName(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.db, "cartonBotTest")

    def testLoadConfigDebug(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.debug, False)

    def testLoadConfigWhitelist(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.whitelisted, ["StreamJar","TestUser2"])

#TESTS FOR REMOVING PERMITS
    def testRemovePermitsExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.removePermits("TestUser1"), True)

    def testRemovePermitsNotExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.removePermits("TestUser0"), False)

#TESTS FOR ADDING PERMITS
    def testAddPermitsExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.addPermits("TestUser3"), True)

    def testAddPermitsNotExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.addPermits("TestUser9"), True)

#TESTS FOR GETTING PERMITS
    def testGetPermitsExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        datetimeObj = datetime.datetime(2009,6,11,8,55,36)
        self.assertEqual(ganon.getPermit("TestUser4"), datetimeObj)

    def testGetPermitsNotExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.getPermit("TestUser11"), None)

#TESTS FOR IS PERMITTED
    def testIsPermittedWhitelist(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.isPermitted("TestUser2"), True)

    def testIsPermittedWhitelistAlt(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.isPermitted("StreamJar"), True)

    def testIsPermittedNotInDB(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.isPermitted("TestUser12"), False)

    def testIsPermittedExpired(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.isPermitted("TestUser5"), False)

    def testIsPermittedNotExpired(self):
        ganon.loadConfig(self.CONFIG_PATH)
        ganon.addPermits("PCarton")
        self.assertEqual(ganon.isPermitted("PCarton"), True)

#TESTS FOR HELPER METHODS
    def testStringToPython(self):
        datetimeObj = datetime.datetime(2010,11,12,18,30,35)
        self.assertEqual(ganon.stringToPython("2010-11-12 18:30:35"), datetimeObj)

    def testPythonToString(self):
        datetimeObj = datetime.datetime(2010,11,12,18,30,35)
        self.assertEqual(ganon.pythonToString(datetimeObj),"2010-11-12 18:30:35")

if __name__ == "__main__":
        unittest.main()
