from DatabaseManagementFactory import DatabaseManagementFactory
from Course import Course

class CourseController:

    def __init__(self):
        self.database_connection = DatabaseManagementFactory.get_database_instance('mariadb')
        self.courses = []
        
    def get_professor_info(self, prof)->bool:
        return True
    
    def get_course_info(self, prof)->bool:
        return True
    
    def get_course_review():
        return

    def create_course(course_name, course_time, section):
        return