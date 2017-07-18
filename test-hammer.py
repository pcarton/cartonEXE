import unittest
from subprocess import call
import datetime
import hammer

class hammerTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

#TESTS FOR IF THE CONFIG LOADED CORRECTLY
    def testLoadConfigAddr(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.dbAddr, "localhost")

    def testLoadConfigPass(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.dbPass, "root")

    def testLoadConfigUser(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.dbUser, "root")

    def testLoadConfigName(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.db, "cartonBotTest")

    def testLoadConfigDebug(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.debug, False)


if __name__ == "__main__":
        unittest.main()
