import Course
import Schedule
import Preferences

#methods and attributes for User class
class User:
    #constructor for User
    def __init__(self, userName, userID,coursesTaken = [], savedSchedules = [], preferences = Preferences.Preferences()):
        self.userName = userName
        self.userID = userID
        self.coursesTaken = coursesTaken
        self.savedSchedules = savedSchedules
        self.preferences = preferences

    #getters and setters for above attributes
    def getUserName(self)->str:
        return self.userName
    
    def setUserName(self,userName):
        self.userName = userName

    def getUserID(self)->int:
        return self.userID
    
    def setUserID(self,id):
        self.userID = id

    def getCoursesTaken(self)->list:
        return self.coursesTaken
    
    def setCoursesTaken(self,courses):
        self.coursesTaken = courses

    def getSavedSchedules(self)->list:
        return self.savedSchedules
    
    def setSavedSchedules(self,schedules):
        self.savedSchedules = schedules

    def getPreferences(self)->Preferences:
        return self.preferences
    
    def setPreferences(self,preferences):
        self.preferences = preferences    
        
    # def addSchedule(self,schedule):
    #     self.savedSchedules.append(schedule)

    # def removeSchedule(self,schedule):
    #     self.savedSchedules.remove(schedule)

    # def addCourse(self,course):
    #     self.coursesTaken.append(course)

    # def removeCourse(self,course):
    #     self.coursesTaken.remove(course)