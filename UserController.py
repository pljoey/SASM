from UserHandler import UserHandler

class UserController:
    def __init__(self):
        self._handler = UserHandler()

    def create_user(self, username, password):
        return self._handler.create_user(username, password)
    
    def find_username(self, username):
        return self._handler.find_user(username)
    
    def login(self, username, password):
        return self._handler.login(username, password)
    
    def logout(self):
        return self._handler.logout()
    
    def delete_user(self, password):
        return self._handler.delete_user(password)
    
    def update_password(self, username, password):
        return self._handler.update_password(username, password)
    
    def add_course(self, course_dept, course_id)->bool:
        return self._handler.add_course(course_dept, course_id)
    
    def remove_course(self, course_name)->bool:
        return self._handler.remove_course(course_name)
    
    def create_schedule(self)->bool:
        return self._handler.create_schedule()
    
    def edit_schedule_name(self, name):
        pass
