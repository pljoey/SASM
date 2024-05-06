import Professor
import Course

#methods and attributes for Blacklist class
class Blacklist:
    #constructor for blacklist class
    def __init__(self):
        self.bl = []

    #returns the blacklist
    def get_blacklist(self)->list:
        return self.bl
    
    def set_blacklist(self, blacklist):
        self.bl = blacklist

    def add_to_course_to_blacklist(self, id, dept):
        name = dept, " ", id 
        self.bl.append(name)

    def add_professor_to_blacklist(self, first, last):
        name = first, " ", last
        self.bl.append(name)

    def remove_course_from_blacklist(self, id, dept):
        name = dept, " ", id
        self.bl.remove(name)

    def remove_professor_from_blacklist(self, first, last):
        name = first, " ", last
        self.bl.remove(name)
