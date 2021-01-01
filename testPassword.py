import unittest
from Password import Password

class TestPasswordModule(unittest.TestCase):    

    def setUp(self):
        self.password= '123_x&5s'.encode('utf-8')
    
    def test_password(self):
        user_hash_pwd = Password.hash_password(self.password)
        self.assertTrue(Password.hash_check(self.password, user_hash_pwd), (True))

if __name__ == '__main__':
    unittest.main()