import Professor

#methods and attributes for Course class
class Course:
    #constructor
    def __init__(self, courseID, courseName, creditHours, isElective, difficultyRating = -1.0, sectionList = {}):
        self.courseID = courseID    
        self.courseName = courseName    
        self.creditHours = creditHours
        self.isElective = isElective
        self.difficultyRating = difficultyRating  
        self.sectionList = sectionList
 
    
    #getter and setter methods for all of the attributes
    def getCourseID(self)->str:
        return self.courseID
    
    def setCourseID(self, id):
        self.courseID = id

    def getCourseName(self)->str:
        return self.courseName
    
    def setCourseName(self, name):
        self.courseName = name

    def getCreditHours(self)->int:
        return self.creditHours
    
    def setCreditHours(self, ch):
        self.creditHours = ch

    def getIsElective(self)->bool:
        return self.isElective
    
    def setIsElective(self,elective):
        self.isElective = elective

    #a value of -1.0 for difficultyRating means that there is no difficultyRating yet
    def getDifficultyRating(self)->float:
        return self.difficultyRating
    
    def setDifficultyRating(self,diff):
        self.difficultyRating = diff

    def getSectionList(self)->dict:
        return self.sectionList
    
    def setSectionList(self,sections):
        self.sectionList = sections
        