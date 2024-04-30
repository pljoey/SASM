import User
import DatabaseManagementFactory

class UserHandler:
    def __init__(self):
        pass

    def create_user(self, username, password, courses_taken):
        user = User(username, password, courses_taken)
        return user
    
    def get_user(self, username, password):
        #get all user information from the database
        DatabaseManagementFactory.get_database_instance("mariadb")
        #create a user object that matches the data from the database
        user = User(username, password, courses_taken, user_id)

    def find_username(self, username):
        DatabaseManagementFactory.get_database_instance("mariadb")
        #check if the username is taken
        #return true if taken false if available

    def check_password(self, username, password):
        DatabaseManagementFactory.get_database_instance("mariabd")
        #check if the password matches with the username
        #return true if match, false if mismatch