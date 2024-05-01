import User
#import exportableFormatHandler
import Schedule
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

    def view_remaining_course(self):
        reqs = {
            "COM 223",
            "ENG 249",
            "IT 168",
            "IT 179",
            "IT 180",
            "IT 191",
            "IT 214",
            "IT 225",
            "IT 261",
            "IT 279",
            "IT 326",
            "IT 327",
            "IT 328",
            "IT 378",
            "IT 383",
            "IT 386",
            "IT 398",
            "MAT 145",
            "MAT 146",
            "MAT 260"
        }
        prevCourses = self.database.get_previous_courses()
        result = []
        for x in reqs:
            if x not in prevCourses:
                result.append(x)
        return result