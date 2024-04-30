import User
#import exportableFormatHandler
import Schedule
from DatabaseManagementFactory import DatabaseManagementFactory

class UserHandler:
    def __init__(self):
        self.aUser
        self.aSched
        self.aData
        pass
                 
    def create_user(self, username, password):
        database_instance = DatabaseManagementFactory.get_database_instance('mariadb')
        hashed_password = hash(password)

        if database_instance.check_user(username):
            return False

        database_instance.create_user(username, hashed_password)
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
        self.aData = None

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