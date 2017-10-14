import unittest
from subprocess import call
import datetime

from .. import hammer

class hammerTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

#TESTS FOR IF THE CONFIG LOADED CORRECTLY
    def testLoadConfigBlacklist(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.blacklist, ["testBlacklist1", "TEST_BLACKLIST2", "TeStBlAcKlIsT3"])

    def testLoadConfigGreylist(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.greylist, ["testGreylist1", "TEST_GREYLIST2", "TeStGrEylIsT3"])

    def testLoadConfigDebug(self):
        hammer.loadConfig(self.CONFIG_PATH)
        self.assertEqual(hammer.debug, False)

    #TODO tests for banCheck, timeoutCheck, and purgeCheck when the criteria is decided
if __name__ == "__main__":
        unittest.main()
