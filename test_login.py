import unittest
from app import LoginSystem


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.system = LoginSystem()


    # Positive Test
    def test_valid_login(self):
        self.assertEqual(
            self.system.login("admin", "Password123!"),
            "Login Successful"
        )

    # Username Validation
    def test_blank_username(self):
        self.assertEqual(
            self.system.login("", "Password123!"),
            "Username Required"
        )

    def test_unknown_user(self):
        self.assertEqual(
            self.system.login("unknown", "Password123!"),
            "User Not Found"
        )

    # Authentication Tests
    def test_wrong_password(self):
        self.assertEqual(
            self.system.login("admin", "WrongPass123!"),
            "Incorrect Password"
        )

    # Password Validation Tests
    def test_blank_password(self):
        self.assertEqual(
            self.system.login("admin", ""),
            "Password Required"
        )

    def test_password_too_short(self):
        self.assertEqual(
            self.system.login("admin", "Ab1!"),
            "Password Too Short"
        )

    def test_password_too_long(self):
        long_password = "A" * 33 + "a1!"
        self.assertEqual(
            self.system.login("admin", long_password),
            "Password Too Long"
        )

    def test_missing_uppercase(self):
        self.assertEqual(
            self.system.login("admin", "password123!"),
            "Password Must Contain Uppercase Letter"
        )

    def test_missing_lowercase(self):
        self.assertEqual(
            self.system.login("admin", "PASSWORD123!"),
            "Password Must Contain Lowercase Letter"
        )

    def test_missing_number(self):
        self.assertEqual(
            self.system.login("admin", "Password!!!"),
            "Password Must Contain Number"
        )

    def test_missing_special_character(self):
        self.assertEqual(
            self.system.login("admin", "Password123"),
            "Password Must Contain Special Character"
        )

    def test_password_contains_space(self):
        self.assertEqual(
            self.system.login("admin", "Password 123!"),
            "Password Cannot Contain Spaces"
        )


if __name__ == "__main__":
    unittest.main()
