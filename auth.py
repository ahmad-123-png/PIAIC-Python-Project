"""
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class AuthSystem:
    def __init__(self):
        # Updated to include 'Ahmad' as an Admin user with the specified password
        self.users = {
            "admin": User("admin", "password", "Admin"),
            "user": User("user", "password", "User"),
            "Ahmad": User("Ahmad", "Qwerty123456", "Admin")  # Added 'Ahmad' with password 'Qwerty123456'
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        else:
            raise ValueError("Invalid username or password")
"""

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class AuthSystem:
    def __init__(self):
        self.users = {
            "admin": User("admin", "password", "Admin"),
            "user": User("user", "password", "User"),
            "Ahmad": User("Ahmad", "Qwerty123456", "Admin")  # Added 'Ahmad' with password 'Qwerty123456'
        
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        else:
            raise ValueError("Invalid username or password")
