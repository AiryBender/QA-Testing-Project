class LoginSystem:

    def __init__(self):
        self.users = {
            "admin": "Password123",
            "qauser": "Testing456",
            "apple": "Retail789"
        }

    def login(self, username, password):

        if username == "":
            return "Username Required"

        if password == "":
            return "Password Required"

        if username not in self.users:
            return "User Not Found"

        if self.users[username] != password:
            return "Incorrect Password"

        return "Login Successful"
