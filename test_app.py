import unittest
from utils import hash_password, verify_password

class TestUtils(unittest.TestCase):
    def test_hash_and_verify_password(self):
        password = "TestPassword123"
        hashed = hash_password(password)
        self.assertTrue(verify_password(hashed, password))
        self.assertFalse(verify_password(hashed, "WrongPassword"))

if __name__ == '__main__':
    unittest.main()
