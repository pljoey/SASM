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