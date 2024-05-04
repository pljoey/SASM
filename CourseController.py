import CourseHandler

class CourseController:

    def __init__(self):
        self._handler = CourseHandler.CourseHandler()
        
    def get_professor_info(self, prof)->bool:
        return True
    
    def get_course_info(self, prof)->bool:
        return True
    
    def get_course_review():
        return

    def create_course(course_name, course_time, section):
        return
    
    def add_custom_course(self,name,start_time,end_time,days)->bool:
        return self._handler.add_custom_course(name,start_time,end_time,days)