import User

class UserHandler:
    def createUser(self, username, password, courses_taken):
        user = User(username, password, courses_taken)
        return user