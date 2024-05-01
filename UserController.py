from UserHandler import UserHandler

class UserController:
    def __init__(self):
        self._handler = UserHandler()

    def create_user(self, username, password):
        return self._handler.create_user(username, password)
    
    def find_username(self, username):
        return self._handler.find_user(username)
    
    def check_password(self, username, password):
        return self._handler.check_password(username, password)
    
    def get_user(self, username, password):
        return self._handler.get_user(username, password)
    
    def update_password(self, username, password):
        return self._handler.update_password(username, password)
    
    def create_schedule(self):
        return self._handler.create_schedule()
    
    def edit_schedule_name(self, name):
        pass
