import User
#import exportableFormatHandler
import Schedule
import Preferences
from DatabaseManagementFactory import DatabaseManagementFactory

class UserHandler:
    def __init__(self):
        self.aUser
        self.aSched
        self.database = DatabaseManagementFactory.get_database_instance('mariadb')
                 
    def create_user(self, username, password):
        hashed_password = hash(password)

        if self.database.check_user(username):
            return False

        self.database.create_user(username, hashed_password)
        return True

    def login(self, username, password):
        database_instance = DatabaseManagementFactory.get_database_instance('mariadb')
        hashed_password = hash(password)

        database_password = database_instance.get_user_pass(username)

        logged_in = not (database_password == None or database_password != hashed_password)

        if logged_in:
            user_id = database_instance._get_user_id(username)
            #TODO: Get rest of use information and add it to User object
            self.aUser = User(username, user_id)
            return True

        else:
            return False
    
    def logout(self):
        self.aUser = None
        self.aSched = None

    def delete_user(self):
        database_instance = DatabaseManagementFactory.get_database_instance('mariadb')

        username = self.aUser.get_user_name()

        self.logout()

        database_instance.delete_user(username)

    def edit_user_preferences(self):
        self.aUser.set_preferences()
        pass

    def create_schedule(self):
        #We should pass a 
        pass

    def edit_schedule(self):
        pass

    def save_schedule_to_database(self):
        pass

    def save_schedule_to_exportable_format(self):
        pass

    def find_user(self, username):
        return self.database.check_user(username)
    
    def check_password(self, username, password):
        hashed_password = hash(password)
        return self.database.check_password(username, hashed_password)
    
    def update_password(self, username, password):
        hashed_password = hash(password)
        self.database.update_password(username, hashed_password)
        courses_taken = self.database.get_previous_courses(username)
        preferences = Preferences(self.database.get_preferred_hours(username), self.database.get_preferred_electives(username), self.database.get_blacklist(username))
        saved_schedule = self.database #add get saved schedule function
        return User(username, courses_taken, saved_schedule, preferences)