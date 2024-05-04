import User
#import exportableFormatFactory
import Preferences
import Schedule
from DatabaseManagementFactory import DatabaseManagementFactory
import hashlib

class UserHandler:
    def __init__(self):
        self.aUser = None
        self.aSched = None

        self.database = DatabaseManagementFactory.get_database_instance('mariadb')
                 
    def create_user(self, username, password):
        new_hash = hashlib.shake_128(password.encode())
        hashed_password = new_hash.hexdigest(10)

        if self.database.check_user(username):
            return False

        self.database.create_user(username, hashed_password)
        return True

    def login(self, username, password):
        new_hash = hashlib.shake_128(password.encode())
        hashed_password = new_hash.hexdigest(10)

        database_password = self.database.get_user_pass(username)

        logged_in = not (database_password == None or database_password != hashed_password)

        if logged_in:
            user_id = self.database._get_user_id(username)
            #TODO: Get rest of use information and add it to User object
            self.aUser = User.User(username, user_id)
            return True

        else:
            return False
    
    def logout(self):
        self.aUser = None
        self.aSched = None

    def delete_user(self, password):
        new_hash = hashlib.shake_128(password.encode())
        hashed_password = new_hash.hexdigest(10)


        username = self.aUser.get_user_name()

        if self.database.check_password(username, hashed_password):
            self.logout()

            self.database.delete_user(username)

            return True
        
        return False
        

    def edit_user_preferences(self):
        self.aUser.set_preferences()
        pass

    def create_schedule(self) -> bool:
        cur_sched = self.aUser.get_current_schedule()
        if(cur_sched == None):
            new_sched = Schedule.Schedule()
            self.aUser.set_current_schedule(new_sched)
            return True
        else:
            return False

    def add_course(self, course_dept, course_id)->bool:
        if self.aUser.get_current_schedule() == None or self.database.check_for_course(course_dept, int(course_id)) == False:
            return False
        else:
            print(course_dept + course_id)
            for Course in self.aUser.get_current_schedule().get_courses():
                if Course.get_course_id() == (course_dept + course_id):
                    return False

    def remove_course(self, course_name)->bool: 
        pass

    def edit_schedule(self):
        pass

    def save_schedule_to_database(self):
        pass

    def save_schedule_to_exportable_format(self):
        pass

    def find_user(self, username):
        return self.database.check_user(username)

    
    def update_password(self, username, password):
        hashed_password = hash(password)
        self.database.update_password(username, hashed_password)
        courses_taken = self.database.get_previous_courses(username)
        preferences = Preferences(self.database.get_preferred_hours(username), self.database.get_preferred_electives(username), self.database.get_blacklist(username))
        saved_schedule = self.database #add get saved schedule function
        return User(username, courses_taken, saved_schedule, preferences)
