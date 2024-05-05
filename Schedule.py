#methods and attributes for the Schedule class
class Schedule:
    #constructor for schedule
    def __init__ (self, name = "",courses = [], tch = 0):
        self.name = name
        #courses in form [(section_num, Course)]
        self.courses = courses
        self.total_credit_hours = tch
        

    #getters for the above attributes
    def get_name(self)->str:
        return self.name
    
    def set_name(self,name):
        self.name = name

    def get_courses(self)->list:
        return self.courses
    
    def set_courses(self, course):
        self.courses = course

    def get_schedule_name(self)->str:
        return self.schedule_name

    def set_schdeule_name(self, name):
        self.schedule_type = name

    def get_total_credit_hours(self)->int:
        return self.total_credit_hours

    def set_total_credit_hours(self, hours):
        self.total_credit_hours = hours

    