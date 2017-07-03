import unittest
import centurion

class centurionTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

    def testLoadConfig(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEquals(centurion.dbAddr, "DBAddrTEST")
        self.assertEquals(centurion.dbPass, "DBPassTEST")
        self.assertEquals(centurion.dbUser, "DBUserTEST")
        self.assertEquals(centurion.db, "DBNameTEST")
        self.assertEquals(centurion.debug, False)

if __name__ == "__main__":
            unittest.main()
