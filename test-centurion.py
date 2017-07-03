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

if __name__ == "__main__":
            unittest.main()
