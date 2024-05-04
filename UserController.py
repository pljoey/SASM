from UserHandler import UserHandler

class UserController:
    def __init__(self):
        self._handler = UserHandler()

    def create_user(self, username, password):
        return self._handler.create_user(username, password)
    
    def login(self, username, password):
        return self._handler.login(username, password)
    
    def logout(self):
        return self._handler.logout()
        
    def delete_user(self, password):
        return self._handler.delete_user(password)
    
    def export_to_format(self):
        return self.export_to_format()
    
    def update_password(self, username, password):
        return self._handler.update_password(username, password)
    
    def create_schedule(self):
        return self._handler.create_schedule()
    
    def edit_schedule_name(self, name):
        pass
