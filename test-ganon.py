import unittest
from subprocess import call

import ganon

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

    def testRemovePermitsExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.removePermits("TestUser1"), True)

    def testRemovePermitsNotExisting(self):
        ganon.loadConfig(self.CONFIG_PATH)
        self.assertEqual(ganon.removePermits("TestUser0"), False)


if __name__ == "__main__":
        unittest.main()
