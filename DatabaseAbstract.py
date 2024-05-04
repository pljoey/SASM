from abc import ABC, abstractmethod

class DatabaseAbstract(ABC):

    @abstractmethod
    def __init__(self):
        self.HOST = None
        self.USER = None
        self.PASSWORD = None
        self.DATABASE = None

    @abstractmethod
    def get_instance(self):
        '''
        Returns the instance of the databse for a singleton pattern
        '''

    @abstractmethod
    def get_user_pass(self, username):
        '''
        Returns the users hashed password
        '''
        pass

    
    @abstractmethod
    def check_user(self, username):
        '''
        Returns true is user is in database
        '''
        pass

    @abstractmethod
    def create_user(self, username, hash_password):
        '''
        Creates a new user from a username and hashed password
        '''
        pass

    @abstractmethod
    def change_password(self, username, hash_password):
        '''
        Updates the users hashed password
        '''
        pass

    @abstractmethod
    def get_preferred_hours(self, username):
        '''
        Returns the number of credit hours that a user prefers
        '''
        pass

    @abstractmethod
    def set_preferred_hours(self, username, hours):
        '''
        Sets the users preferred credit hours in the database
        '''
        pass

    @abstractmethod
    def add_course(self, department, course_num, description, course_name, credit_hours):
        '''
        adds a course to the database
        '''
        pass

    @abstractmethod
    def get_course_description(self, department, course_num):
        '''
        Returns the description from a course
        '''
        pass

    @abstractmethod
    def get_course_credit_hours(self, department, course_num):
        '''
        Returns the number of credit hours for a course
        '''

    @abstractmethod
    def add_professor(self, first_name, last_name, title, department):
        '''
        Adds a professor to the database
        '''
        pass

    @abstractmethod
    def add_section(self, section_num, professor_first, professor_last, professor_dept, department, course_num, start_time, end_time):
        '''
        adds a section of a course to the database
        '''
        pass

    @abstractmethod
    def get_sections(self, department, course_num):
        '''
        Returns a list of all sections numbers
        '''

    @abstractmethod
    def get_section_details(self, department, course_num, section_num):
        '''
        Returns the Details of a section
        '''
    
    @abstractmethod
    def add_course_to_blacklist(self, username, department, course_num):
        '''
        adds a course to the users blacklist
        '''
        pass

    @abstractmethod
    def add_professor_to_blacklist(self, username, professor_first, professor_last, professor_dept):
        '''
        adds a professor to the users blacklist
        '''
        pass

    @abstractmethod
    def remove_course_from_blacklist(self, username, department, course_num):
        '''
        Removes a course from the users blacklist
        '''
        pass

    @abstractmethod
    def remove_professor_from_blacklist(self, username, professor_first, professor_last, professor_dept):
        '''
        Removes a profess from the users blacklist
        '''
        pass

    @abstractmethod
    def get_blacklist(self, username):
        '''
        Returns the users blacklist
        '''
        pass

    @abstractmethod
    def add_to_previous_courses(self, username, department, course_num):
        '''
        adds a course to the previously taken courses
        '''
        pass

    @abstractmethod
    def remove_from_previous_courses(self, username, department, course_num):
        '''
        removes a course from the previous courses
        '''
        pass 

    @abstractmethod
    def get_previous_courses(self, username):
        '''
        Returns a list of the users previous courses
        '''
        pass

    @abstractmethod
    def add_to_preferred_electives(self, username, department, course_num):
        '''
        Adds a course to the preferred electives table
        '''
        pass

    @abstractmethod
    def remove_from_preferred_electives(self, username, department, course_num):
        '''
        Removes a course from the preferred electives table
        '''
        pass

    @abstractmethod
    def get_preferred_electives(self, username):
        '''
        Returns a users preferred electives
        '''
        pass

    @abstractmethod
    def delete_user(self, username):
        '''
        Deletes all user information from database
        '''

    @abstractmethod
    def check_for_course(self, department, course_num):
        '''
        Returns true if course exists in database
        '''

    @abstractmethod
    def add_course_prereqs(self, course_dept, course_num, prereq_dept, prereq_num):
        '''
        Adds a prerequisite course to another course
        '''
    
    @abstractmethod
    def get_course_prereqs(self, course_dept, course_num):
        '''
        Returns a list of courses that are a prerequisite for the input course
        '''

    @abstractmethod
    def create_schedule(self, username, name=None):
        '''
        Creates a schedule in the database
        '''
    
    @abstractmethod
    def edit_schedule_name(self, username, old_name, new_name):
        '''
        Renames a schedule in the database
        '''

    @abstractmethod
    def delete_schedule(self, username, schedule_name):
        '''
        Deletes a schedule from the database
        '''

    @abstractmethod
    def get_user_schedule_names(self, username):
        '''
        Returns a list of schedule names for a user
        '''

    @abstractmethod
    def add_section_to_schedule(self, username, schedule_name, course_dept, course_num, section_num):
        '''
        Adds a section to a schedule
        '''
    @abstractmethod
    def remove_section_from_schedule(self, username, schedule_name, course_dept, course_num, section_num):
        '''
        Removes a section from a schedule
        '''

    @abstractmethod
    def get_sections_from_schedule(self, username, schedule_name):
        '''
        Gets a list of sections that are in a schedule
        '''