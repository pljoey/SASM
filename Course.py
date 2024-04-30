import Professor

#methods and attributes for Course class
class Course:
    #constructor
    def __init__(self, course_id, course_name, credit_hours, is_elective, difficulty_rating = -1.0, section_list = {}):
        self.course_id = course_id    
        self.course_name = course_name    
        self.credit_hours = credit_hours
        self.is_elective = is_elective
        self.difficulty_rating = difficulty_rating  
        self.section_list = section_list
 
    
    #getter and setter methods for all of the attributes
    def get_course_id(self)->str:
        return self.course_id
    
    def set_course_id(self, id):
        self.course_id = id

    def get_course_name(self)->str:
        return self.course_name
    
    def set_course_name(self, name):
        self.course_name = name

    def get_credit_hours(self)->int:
        return self.credit_hours
    
    def set_credit_hours(self, ch):
        self.creditHours = ch

    def ge_is_elective(self)->bool:
        return self.isElective
    
    def set_is_elective(self,elective):
        self.is_elective = elective

    #a value of -1.0 for difficultyRating means that there is no difficultyRating yet
    def get_difficulty_rating(self)->float:
        return self.difficulty_rating
    
    def set_difficulty_rating(self,diff):
        self.difficulty_rating = diff

    def get_section_list(self)->dict:
        return self.section_list
    
    def set_section_list(self,sections):
        self.section_list = sections
        