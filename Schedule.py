import Semester

#methods and attributes for the Schedule class
class Schedule:
    #constructor for schedule
    def __init__ (self,semesters = []):
        self.semesters = semesters
        self.scheduleType = self.determineScheduleType()

    #getters for the above attributes
    def getSemesters(self)->list:
        return self.semesters
    
    #no setters for semesters because its a list. Instead, it has add and remove semester methods
    def addSemester(self,semester):
        self.semesters.append(semester)
        self.scheduleType = self.determineScheduleType()

    def removeSemester(self,semester):
        self.semesters.remove(semester)
        self.scheduleType = self.determineScheduleType()

    def getScheduleType(self)->str:
        return self.scheduleType

    #determines the scheduleType based on the number of semesters
    def determineScheduleType(self)->str:
        if(len(self.semesters) == 0):
            return "empty schedule"
        elif(len(self.semesters) == 1):
            return "short schedule"
        else:
            return "long schedule"
        


    