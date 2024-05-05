#methods and attributes for the Schedule class
class Schedule:
    #constructor for schedule
    def __init__ (self, name = "", sections = [], tch = 0):
        self.name = name
        self.sections = sections
        self.total_credit_hours = tch
        

    #getters for the above attributes
    def get_name(self)->str:
        return self.name
    
    def set_name(self,name):
        self.name = name
    
    def add_section(self, course, section_id):
        self.sections.append((course, section_id))

    def remove_section(self, course, section_id):
        self.sections.remove((course, section_id))

    def get_sections(self):
        return self.sections

    def get_schedule_name(self)->str:
        return self.schedule_name

    def set_schdeule_name(self, name):
        self.schedule_type = name

    def get_total_credit_hours(self)->int:
        return self.total_credit_hours

    def set_total_credit_hours(self, hours):
        self.total_credit_hours = hours

    