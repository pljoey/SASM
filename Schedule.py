import Semester

#methods and attributes for the Schedule class
class Schedule:
    #constructor for schedule
    def __init__ (self,semesters = [], name = ""):
        self.semesters = semesters
        self.schedule_name = name

    #getters for the above attributes
    def get_semesters(self)->list:
        return self.semesters
    
    def set_semesters(self, semester):
        self.semesters = semester

    def get_schedule_name(self)->str:
        return self.schedule_name

    def set_schdeule_name(self, name):
        self.schedule_type = name

    