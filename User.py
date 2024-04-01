import Course
import Schedule
import Preferences

#methods and attributes for User class
class User:
    #constructor for User
    def __init__(self, userName, password, coursesTaken = []):
        self._userName = userName
        self._password = password
        self._USERID = 1 #this will get a new value from the database. it will be the highest known userID + 1
        self._coursesTaken = coursesTaken
        #self.savedSchedules = savedSchedules
        self._preferences = Preferences(coursesTaken)

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
    
    #no setter for coursesTaken because its a list. Instead it has add and remove course methods
    def addCourse(self,course):
        self.coursesTaken.append(course)

    def removeCourse(self,course):
        self.coursesTaken.remove(course)

    def getSavedSchedules(self)->list:
        return self.savedSchedules
    
    #no setter for savedSchedule because its a list. Instead it has add and remove schedule methods
    def addSchedule(self,schedule):
        self.savedSchedules.append(schedule)

    def removeSchedule(self,schedule):
        self.savedSchedules.remove(schedule)

    def getPreferences(self)->Preferences:
        return self.preferences
    
    def setPreferences(self,preferences):
        self.preferences = preferences