from Handlers import UserHandler

class UserController:
    def __init__(self):
        pass

    def create_user(self, username, password, courses_taken = []):
        handler = UserHandler()
        return handler.createUser(username, password, courses_taken)
    
    def get_user(self, username, password):
        pass