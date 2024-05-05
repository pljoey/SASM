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
    
    def add_course(self, course_dept, course_id)->bool:
        return self._handler.add_course(course_dept, course_id)
    
    def remove_course(self, course_dept, course_id)->bool:
        return self._handler.remove_course(course_dept, course_id)
    
    def create_schedule(self)->bool:
        return self._handler.create_schedule()
    
    def delete_schedule(self)->bool:
        return self._handler.delete_schedule()
    
    def edit_schedule_name(self, name):
        pass

    def view_remaining_courses(self):
        return self._handler.view_remaining_courses()
    
    def add_previous_courses(self,course)->bool:
        return self._handler.add_previous_courses(course)

    def remove_previous_course(self,course)->bool:
        return self._handler.remove_previous_course(course)
    
    def save_schedule(self):
        self._handler.save_schedule_to_database()