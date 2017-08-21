import unittest
from subprocess import call
import datetime
import scribe

class scibeTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

#TESTS FOR IF THE CONFIG LOADED CORRECTLY
    def testLoadConfigLogFile(self):
        scribe.loadConfig(self.CONFIG_PATH)
        self.assertEqual(scibe.logFile, "testLog")

    def testLoadConfigLogFile(self):
        scribe.loadConfig(self.CONFIG_PATH)
        self.assertEqual(scibe.logExtension, "txt")

    def testLoadConfigDebug(self):
        scribe.loadConfig(self.CONFIG_PATH)
        self.assertEqual(scibe.debug, False)

    #TODO rest of tests
if __name__ == "__main__":
        unittest.main()
