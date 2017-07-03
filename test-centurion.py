import unittest
import centurion

class centurionTest(unittest.TestCase):
    def setUp(self):
        self.CONFIG_PATH = 'config-test.json'

    def testLoadConfig(self):
        centurion.loadConfig(self.CONFIG_PATH)
        self.assertEqual(centurion.dbAddr, "DBAddrTEST")
        self.assertEqual(centurion.dbPass, "DBPassTEST")
        self.assertEqual(centurion.dbUser, "DBUserTEST")
        self.assertEqual(centurion.db, "DBNameTEST")
        self.assertEqual(centurion.debug, False)

if __name__ == "__main__":
            unittest.main()
