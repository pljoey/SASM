from Handlers import UserHandler

class UserController:
    def __init__(self):
        self._handler = UserHandler()

    def create_user(self, username, password, courses_taken = []):
        return self._handler.create_user(username, password, courses_taken)
    
    def find_user(self, username):
        return self._handler.find_user(username)
    
    def check_password(self, username, password):
        return self._handler.check_password(username, password)
    
    def get_user(self, username, password):
        return self._handler.get_user(username, password)