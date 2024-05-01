import Professor

#methods and attributes for Course class
class Course:
    #constructor
    def __init__(self, course_id, course_name, credit_hours, is_elective, difficulty_rating = -1.0, section_dict = {}):
        self.course_id = course_id    
        self.course_name = course_name    
        self.credit_hours = credit_hours
        self.is_elective = is_elective
        self.section_dict = section_dict
 
    
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

    def get_section_dict(self)->dict:
        return self.section_dict
    
    def set_section_dict(self,sections):
        self.section_dict = sections

    def add_section(self, section_num, prof, start_time, end_time, monday = False, tuesday = False, wednesday = False, thursday = False, friday = False):
        self.section_dict.update({section_num:(prof, start_time,end_time,monday,tuesday,wednesday,thursday,friday)})

    def remove_section(self, section_num):
        self.section_dict.delete(section_num)

    def get_section(self, section_num)->tuple[Professor.Professor, float, float, bool, bool, bool, bool, bool]:
        return self.section_dict.get(section_num)
        