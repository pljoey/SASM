import Professor
import Course

#methods and attributes for Blacklist class
class Blacklist:
    #constructor for blacklist class
    def __init__(self):
        self.blacklist = []

    #returns the blacklist
    def getBlacklist(self)->list:
        return self.blacklist
    
    def setBlacklist(self, blacklist):
        self.blacklist = blacklist

    #adds an item to the blacklist
    # def addToBlacklist(self, blacklisted):
    #     self.blacklist.append(blacklisted)

    # #removes an item from the blacklist
    # def removeFromBlacklist(self, unBlacklisted):
    #     self.blacklist.remove(unBlacklisted)