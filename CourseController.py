from CourseHandler import CourseHandler

class CourseController:

    def __init__(self):
        self._course_handler = CourseHandler()

    def get_professor_info(self, prof)->bool:
        return self._course_handler.get_professor_information(prof)
    
    def get_course_info(self, prof)->bool:
        return True
    
    def get_course_review():
        return

    def create_course(course_name, course_time, section):
        return