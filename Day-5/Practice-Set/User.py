# Create class User with private password.\

class User:

    def __init__(self, username):
        self.username = username
        self.__password = ""

    def setPassword(self, password):
        if len(password) >= 6:
            self.__password = password
            print("Password set successfully.")
        else:
            print("Password must be at least 6 characters long!")

    def getPassword(self):
        return self.__password
    
user1 = User("john_doe")
user1.setPassword("secret123")
print(f"Username: {user1.username}, Password: {user1.getPassword()}")
