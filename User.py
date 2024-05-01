import Course
import Schedule
import Preferences

#methods and attributes for User class
class User:
    #constructor for User
    def __init__(self, user_name,courses_taken = [], saved_schedules = [], preferences = Preferences.Preferences()):
        self.user_name = user_name
        self.courses_taken = courses_taken
        self.saved_schedules = saved_schedules
        self.preferences = preferences

    #getters and setters for above attributes
    def get_user_name(self)->str:
        return self.user_name
    
    def set_user_name(self,user_name):
        self.user_name = user_name

    def get_courses_taken(self)->list:
        return self.courses_taken
    
    def set_courses_taken(self,courses):
        self.courses_taken = courses

    def get_saved_schedules(self)->list:
        return self.saved_schedules
    
    def set_saved_schedules(self,schedules):
        self.saved_schedules = schedules

    def get_preferences(self)->Preferences:
        return self.preferences
    
    def set_preferences(self,preferences):
        self.preferences = preferences    