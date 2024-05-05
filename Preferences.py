import Blacklist

#methods and attributes for the preferences class
class Preferences:
    #constructor for Preferences class
    def __init__(self, preferred_credit_hours = 15, preferred_electives = [], local_blacklist = Blacklist.Blacklist()):
        self.preferred_credit_hours = preferred_credit_hours
        self.preferred_electives = preferred_electives
        self.local_blacklist = local_blacklist
    
    #getters and setters for the above attributes
    def get_preferred_credit_hours(self)->int:
        return self.preferred_credit_hours
    
    def set_preferred_credit_hours(self,credit_hours):
        self.preferred_credit_hours = credit_hours

    def get_preferred_electives(self)->list:
        return self.preferred_electives
    
    def set_preferred_electives(self, electives):
        self.preferred_electives = electives
    
    def get_local_blacklist(self)->Blacklist:
        return self.local_blacklist
    
    def set_local_blacklist(self,blacklist):
        self.local_blacklist = blacklist   