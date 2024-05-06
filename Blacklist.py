import Professor
import Course

#methods and attributes for Blacklist class
class Blacklist:
    #constructor for blacklist class
    def __init__(self):
        self.blacklist = []

    #returns the blacklist
    def get_blacklist(self)->list:
        return self.blacklist
    
    def set_blacklist(self, blacklist):
        self.blacklist = blacklist

    def add_to_course_to_blacklist(self, id, dept):
        name = dept, " ", id 
        self.blacklist.append(name.upper())

    def add_professor_to_blacklist(self, first, last):
        name = first, " ", last
        self.blacklist.append(name.upper())

    def remove_course_from_blacklist(self, id, dept):
        name = dept, " ", id
        self.blacklist.remove(name.upper())

    def remove_professor_from_blacklist(self, first, last):
        name = first, " ", last
        self.blacklist.remove(name.upper())
