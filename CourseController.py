import CourseHandler
from Course import Course

class CourseController:

    def __init__(self):
        self._handler = CourseHandler.CourseHandler()
        self.courses = []

        
    def get_professor_info(self, prof):
        return prof
        
    def get_course_info(self, course):
        return self._handler.get_course_info(course)
    
    def get_course_hours(self,course):
        return self._handler.get_course_hours(course)

    def create_course(course_name, course_time, section):
        return
    
    def add_custom_course(self,name,start_time,end_time,days)->bool:
        return self._handler.add_custom_course(name,start_time,end_time,days)