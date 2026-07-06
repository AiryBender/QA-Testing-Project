import re


class LoginSystem:

    def __init__(self):
        self.users = {
            "admin": "Password123!",
            "user": "Testing456@",
            "tester": "HireMe789#"
        }

    def validate_password(self, password):

        if password == "":
            return "Password Required"

        if len(password) < 8:
            return "Password Too Short"

        if len(password) > 32:
            return "Password Too Long"

        if not re.search(r"[A-Z]", password):
            return "Password Must Contain Uppercase Letter"

        if not re.search(r"[a-z]", password):
            return "Password Must Contain Lowercase Letter"

        if not re.search(r"\d", password):
            return "Password Must Contain Number"

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "Password Must Contain Special Character"

        if re.search(r"\s", password):
            return "Password Cannot Contain Spaces"

        return "Valid"

    def login(self, username, password):

        if username == "":
            return "Username Required"

        validation = self.validate_password(password)

        if validation != "Valid":
            return validation

        if username not in self.users:
            return "User Not Found"

        if self.users[username] != password:
            return "Incorrect Password"

        return "Login Successful"
