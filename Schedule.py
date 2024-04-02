import Semester

#methods and attributes for the Schedule class
class Schedule:
    #constructor for schedule
    def __init__ (self,semesters = [], type = ""):
        self.semesters = semesters
        self.scheduleType = type

    #getters for the above attributes
    def getSemesters(self)->list:
        return self.semesters
    
    def setSemesters(self, semester):
        self.semesters = semester

    def getScheduleType(self)->str:
        return self.scheduleType

    def setSchdeuleType(self, type):
        self.scheduleType = type

    # def addSemester(self,semester):
    #     self.semesters.append(semester)
    #     self.scheduleType = self.determineScheduleType()

    # def removeSemester(self,semester):
    #     self.semesters.remove(semester)
    #     self.scheduleType = self.determineScheduleType()

    # #determines the scheduleType based on the number of semesters
    # def determineScheduleType(self)->str:
    #     if(len(self.semesters) == 0):
    #         return "empty schedule"
    #     elif(len(self.semesters) == 1):
    #         return "short schedule"
    #     else:
    #         return "long schedule"
    