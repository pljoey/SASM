import User
import ExportableFormatFactory
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
            #TODO: Get rest of use information and add it to User object
            previous_courses = self.database.get_previous_courses(username)
            preferred_credit_hours = self.database.get_preferred_hours(username)
            blacklist = self.database.get_blacklist(username)

            self.database.get_blacklist(username)
            self.aUser = User.User(username, courses_taken=self.database.get_previous_courses(username))
            return True

        return False
    
    def logout(self):
        # Adding functionality
        ## If someone logs out it will update the user's preferences, courses taken, and schedule
        self.aUser = None
        self.aSched = None
        return (True)

    def export_to_format(self):
        text_export = ExportableFormatFactory.get_format_instance_type('text')

        schedule = self.aUser.current_schedule

        text_export.export(schedule)

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
        schedules = self.database.get_user_schedule_names(self.aUser.get_user_name())
        if schedules == None and cur_sched == None:
            new_sched = Schedule.Schedule()
            self.aUser.set_current_schedule(new_sched)
            self.database.create_schedule(self.aUser.get_user_name())
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
            #TODO implement checks to make sure that the course can be added to the schedule
            schedule = self.aUser.get_schedule()


    def remove_course(self, course_dept, course_id)->bool: 
        #TODO figure out how this is supposed to work
        return self.database.remove_section_from_schedule(self.aUser.get_user_name, self.aUser.get_current_schedule().get_name(), course_dept, course_id,  )

    
    def delete_schedule(self)->bool:
        #TODO this should work once all of the data is retrieved for the user during login
        schedules = self.database.get_user_schedule_names(self.aUser.get_user_name())
        if self.aUser != None:
            self.aUser.set_current_schedule(None)
        if schedules != None:
            for schedule in schedules:
                self.database.delete_schedule(self.aUser.get_user_name(), schedule)
            return True
        else:
            print("No schedule exists")
            return False

    def edit_schedule(self):
        pass

    def save_schedule_to_database(self):
        pass

    def save_schedule_to_exportable_format(self):
        pass
    
    def update_password(self, username, password):
        hashed_password = hash(password)
        self.database.update_password(username, hashed_password)
        courses_taken = self.database.get_previous_courses(username)
        preferences = Preferences(self.database.get_preferred_hours(username), self.database.get_preferred_electives(username), self.database.get_blacklist(username))
        saved_schedule = self.database #add get saved schedule function
        return User(username, courses_taken, saved_schedule, preferences)


    def view_remaining_courses(self):
        reqs = {"COM 223",  "ENG 249","IT 168","IT 179","IT 180","IT 191","IT 214","IT 225","IT 261","IT 279","IT 326", "IT 327","IT 328","IT 378","IT 383","IT 386","IT 398","MAT 145", "MAT 146","MAT 260"}
        prevCourses = self.database.get_previous_courses()
        result = []
        for x in reqs:
            if x not in prevCourses:
                result.append(x)
        return result
    
    def view_prior_courses(self):
        return self.database.get_previous_courses()

    def add_previous_courses(self,course)->bool:
        #takes a string like 'IT 326'
        taken = self.database.get_previous_courses()
        c_Split = course.split()
        if self.database.check_for_course(course) and course not in taken:
            taken.append(course)
            self.database.add_to_previous_courses(self.aUser.get_user_name(),c_Split.pop(0),c_Split.pop(0))
            return True
        return False

    def remove_previous_course(self, course)->bool: 
        taken = self.database.get_previous_courses()
        c_Split = course.split()
        if self.database.check_for_course(course) and course not in taken:
            taken.remove(course)
            self.database.remove_from_previous_courses(self.aUser.get_user_name(),c_Split.pop(0),c_Split.pop(0))
            return True
        return False 