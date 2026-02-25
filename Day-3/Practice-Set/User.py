# Create class User and count number of users created.

class User:
    count = 0

    def __init__(self):
        User.count += 1

user1 = User();
user2 = User();

print(User.count)