import Course

#methods and attributes for Semester class
class Semester:
    #constructor for Semester class
    def __init__(self, sememster_id, courses = [], semester_difficulty = -1.0, total_credit_hours = 0.0):
        self.semester_id = sememster_id
        self.courses = courses
        self.semester_difficulty = semester_difficulty
        self.total_credit_hours = total_credit_hours

    #getters and setters for the above attributes
    def get_semester_id(self)->str:
        return self.semester_id
    
    def set_semester_id(self,id):
        self.semester_id = id

    def get_courses(self)->list:
        return self.courses
    
    def set_courses(self, courses):
        self.courses = courses
    
    def get_semester_difficulty(self)->float:
        return self.semester_difficulty 

    def set_semester_difficulty(self, difficulty):
        self.semester_difficulty = difficulty

    def get_total_credit_hours(self)->int:
        return self.total_credit_hours
    
    def setTotalCreditHours(self, creditHours):
        self.totalCreditHours = creditHours
