import unittest
from app import LoginSystem


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.system = LoginSystem()

    # Positive Test

    def test_valid_login(self):
        result = self.system.login("admin", "Password123")
        self.assertEqual(result, "Login Successful")

    # Negative Tests

    def test_wrong_password(self):
        result = self.system.login("admin", "WrongPassword")
        self.assertEqual(result, "Incorrect Password")

    def test_unknown_user(self):
        result = self.system.login("unknown", "Password123")
        self.assertEqual(result, "User Not Found")

    def test_blank_username(self):
        result = self.system.login("", "Password123")
        self.assertEqual(result, "Username Required")

    def test_blank_password(self):
        result = self.system.login("admin", "")
        self.assertEqual(result, "Password Required")

    def test_blank_both(self):
        result = self.system.login("", "")
        self.assertEqual(result, "Username Required")


if __name__ == "__main__":
    unittest.main()
