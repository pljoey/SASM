from abc import ABC, abstractmethod

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