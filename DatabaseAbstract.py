from abc import ABC, abstractmethod
from datetime import time

class DatabaseAbstract(ABC):

    @abstractmethod
    def __init__(self):
        self.HOST = None
        self.USER = None
        self.PASSWORD = None
        self.DATABASE = None

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
    def add_course(self, department, course_num, description):
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
        Returns a list of all sections and their professor for a specific course
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

