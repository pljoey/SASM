import Blacklist

#methods and attributes for the preferences class
class Preferences:
    #constructor for Preferences class
    def __init__(self, preferredCreditHours = -1, preferredElectives = [], localBlacklist = Blacklist.Blacklist()):
        self.preferredCreditHours = preferredCreditHours
        self.preferredElectives = preferredElectives
        self.localBlacklist = localBlacklist
    
    #getters and setters for the above attributes
    def getPreferredCreditHours(self)->int:
        return self.preferredCreditHours
    
    def setPreferredCreditHours(self,creditHours):
        self.preferredCreditHours = creditHours

    def getPreferredElectives(self)->list:
        return self.preferredElectives
    
    def setPreferredElectives(self, electives):
        self.preferredElectives = electives
    
    def getLocalBlacklist(self)->Blacklist:
        return self.localBlacklist
    
    def setLocalBlacklist(self,blacklist):
        self.localBlacklist = blacklist   

    #add and remove methods for preferredElectives
    # def addElective(self,elective):
    #     self.preferredElectives.append(elective)

    # def removeElective(self,elective):
    #     self.preferredElectives.remove(elective)

    # #add and remove methods for preferredElectives
    # def addBlacklistedItems(self,itemList):
    #     for item in itemList:
    #         self.localBlacklist.addToBlacklist(item)

    # def removeBlacklistedItems(self,itemList):
    #     for item in itemList:
    #         self.localBlacklist.removeFromBlacklist(item)