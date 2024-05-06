import User
from ExportableFormatFactory import ExportableFormatFactory
import Preferences
from Schedule import Schedule
from Course import Course
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

            prof_blacklist = blacklist[1]
            course_blacklist = blacklist[0]

            self.database.get_blacklist(username)
            self.aUser = User.User(username, courses_taken=previous_courses)

            self.aUser.preferences.set_preferred_credit_hours(preferred_credit_hours)

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
        if cur_sched == None:
            new_sched = Schedule()
            self.aUser.set_current_schedule(new_sched)
            self.aSched = self.aUser.get_current_schedule()
            #self.database.create_schedule(self.aUser.get_user_name())
            return True
        else:
            return False

    def add_course(self, course_dept, course_id)->bool:
        schedule = self.aSched
        if schedule == None:
            print("no schedule is loaded")
            return False
        elif self.database.check_for_course(course_dept, int(course_id)) == False: 
            print("course does not exist")

            return False
        elif (course_dept + " " + course_id) in (schedule.get_courses()):
            print("course already in schedule")
            return False
        else:
            current_course_list = schedule.get_courses()
            current_course_list.append(course_dept + " " + course_id)
            schedule.set_courses(current_course_list)
            self.aUser.set_current_schedule(schedule)
            self.aSched = self.aUser.get_current_schedule()
            return True         
                            

    def remove_course(self, course_dept, course_id)->bool: 
        if(self.aSched == None):
            return False
        elif (course_dept + " " + course_id) in self.aSched.get_courses():
            self.aSched.get_courses().remove(course_dept + " " + course_id)
            self.aUser.set_current_schedule(self.aSched)
            return True
        else:
            print("Course is not in schedule")
            return False
    
    def delete_schedule(self)->bool:
        schedules = self.database.get_user_schedule_names(self.aUser.get_user_name())
        if schedules != None:
            for schedule in schedules:
                self.database.delete_schedule(self.aUser.get_user_name(), schedule)
            self.aSched = None
            self.aUser.set_current_schedule(None)
            return True
        else:
            print("No schedule exists")
            return False

    def edit_schedule(self):
        pass

    def clear_schedule(self):
        self.aUser.set_current_schedule(None)

    def save_schedule_to_database(self):
        cur_schedule = self.aUser.get_current_schedule().get_courses()
        name = self.database.create_schedule(self.aUser.get_user_name())
        for cur_course in cur_schedule:
            print(cur_course)
            cur_course_split = cur_course.split(" ")
            self.database.add_section_to_schedule(self.aUser.get_user_name(), name, cur_course_split[0], cur_course_split[1])

    def get_schedule_names(self):
        print("Here are all schedules saved to your account:")
        schedule_names = self.database.get_user_schedule_names(self.aUser.get_user_name())

        for schedule_name in schedule_names:
            print(schedule_name[0])

    def load_schedule(self, name):
        build_new_schedule = []
        sched = self.database.get_sections_from_schedule(self.aUser.get_user_name(), name)
        for course in sched:
            build_new_schedule.append(course[0])
        print(build_new_schedule)
        self.aUser.set_current_schedule(build_new_schedule) 

    def save_schedule_to_exportable_format(self):
        pass
    
    def update_password(self, username, password):
        new_hash = hashlib.shake_128(password.encode())
        hashed_password = new_hash.hexdigest(10)
        self.database.change_password(username, hashed_password)

    def fill_schedule(self):
        pref_cred_hours = self.aUser.get_preferences().get_preferred_credit_hours()
        cur_cred_hours = 0
        blacklisted = self.aUser.get_preferences().get_local_blacklist()
        result = []
        prev_courses = self.database.get_previous_courses(self.aUser.get_user_name())
        classes_remaining = self.view_remaining_courses()
        for cur_class in classes_remaining:
            cur_class_split = cur_class.split(" ")
            course_prereq = self.database.get_course_prereqs(cur_class_split[0], cur_class_split[1])
            if (course_prereq == [] or course_prereq[0] in prev_courses):
                result.append(cur_class)
                cur_cred_hours += self.database.get_course_credit_hours(cur_class_split[0], cur_class_split[1])
            if(cur_cred_hours >= pref_cred_hours):
                break
        self.aSched.set_courses(result)
        self.aUser.set_current_schedule(self.aSched)

    def view_schedule(self):
        try:
            return self.aUser.get_current_schedule().get_courses()
        except:
            return "No current schedule selected"

    def view_remaining_courses(self):
        reqs = {"COM 223",  "ENG 249","IT 168","IT 179","IT 180","IT 191","IT 214","IT 225","IT 261","IT 279","IT 326", "IT 327","IT 328","IT 378","IT 383","IT 386","IT 398","MAT 145", "MAT 146","MAT 260"}
        prevCourses = self.database.get_previous_courses(self.aUser.get_user_name())
        result = []
        for x in reqs:
            if x not in prevCourses:
                result.append(x)
        return result
    
    def view_prior_courses(self):
        return self.database.get_previous_courses(self.aUser.get_user_name())

    def add_previous_courses(self,course)->bool:
        #takes a string like 'IT 326'
        taken = self.database.get_previous_courses(self.aUser.get_user_name())
        c_Split = course.split()
        if(len(c_Split) == 2):
            dep = c_Split.pop(0)
            num = c_Split.pop(0)
            if self.database.check_for_course(dep,num) and course not in taken:
                taken.append(course)
                self.database.add_to_previous_courses(self.aUser.get_user_name(),dep,num)
                return True
        return False

    def remove_previous_course(self, course)->bool: 
        taken = self.database.get_previous_courses(self.aUser.get_user_name())
        c_Split = course.split()
        if(len(c_Split) == 2):
            dep = c_Split.pop(0)
            num = c_Split.pop(0)
            if self.database.check_for_course(dep,num) and course in taken:
                taken.remove(course)
                self.database.remove_from_previous_courses(self.aUser.get_user_name(),dep,num)
                return True
        return False 
    
    def add_course_to_blacklist(self, course_id, course_dept):
        self.database.add_course_to_blacklist(self.aUser.get_user_name(), course_dept, course_id)
    
    def add_professor_to_blacklist(self, professor_first, professor_last, professor_dept):
        self.database.add_professor_to_blacklist(self.aUser.get_user_name(), professor_first, professor_last, professor_dept)
    
    def remove_course_from_blacklist(self, course_id, course_dept):
        self.database.remove_course_from_blacklist(self.aUser.get_user_name(),course_dept, course_id )

    def remove_professor_from_blacklist(self, professor_first, professor_last, professor_dept):
        self.database.remove_professor_from_blacklist(self.aUser.get_user_name(), professor_first, professor_last, professor_dept)

    def view_blacklist(self):
        return self.database.get_blacklist(self.aUser.get_user_name())