import Course
import Schedule
import Preferences

#methods and attributes for User class
class User:
    #constructor for User
    def __init__(self, user_name, courses_taken = [], current_schedule = None, preferences = Preferences.Preferences()):
        self.user_name = user_name
        self.courses_taken = courses_taken
        self.current_schedule = current_schedule
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

    def get_current_schedule(self)->Schedule:
        return self.current_schedule
    
    def set_current_schedule(self,schedule):
        self.current_schedule = schedule

    def get_preferences(self)->Preferences.Preferences:
        return self.preferences
    
    def set_preferences(self,preferences):
        self.preferences = preferences    