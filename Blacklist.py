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

    def add_To_Blacklist(self, course): 
        self.blacklist.append(course)

    def add_To_Blacklist(self, professor):
        self.blacklist.append(professor)

    def remove_From_Blacklist(self, course):
        self.blacklist.remove(course)

    def remove_From_Blacklist(self, professor):
        self.blacklist.remove(professor)
