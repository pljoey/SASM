import Semester

#methods and attributes for the Schedule class
class Schedule:
    #constructor for schedule
    def __init__ (self,semesters = [], type = ""):
        self.semesters = semesters
        self.schedule_type = type

    #getters for the above attributes
    def get_semesters(self)->list:
        return self.semesters
    
    def set_semesters(self, semester):
        self.semesters = semester

    def get_schedule_type(self)->str:
        return self.schedule_type

    def set_schdeule_type(self, type):
        self.schedule_type = type

    