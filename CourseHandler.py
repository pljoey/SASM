from DatabaseManagementFactory import DatabaseManagementFactory

class CourseHandler:

    def __init__(self):
        self._database_instance = DatabaseManagementFactory.get_database_instance("mariadb")

    def create_course(course_name, course_time, section):
        pass

    def get_course_section_review(section):
        return
    
    def get_professor_information(self, prof):
        prof_id = self._database_instance._get_prof_id(prof)
        self._database_instance.get_professor(prof_id)