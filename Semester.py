import Course

#methods and attributes for Semester class
class Semester:
    #constructor for Semester class
    def __init__(self, sememsterID, courses = []):
        self.semesterID = sememsterID
        self.courses = courses
        self.semesterDifficulty = self.calculateSemesterDifficulty()
        self.totalCreditHours = self.calculateTotalCreditHours()

    #getters and setters for the above attributes
    def getSemesterID(self)->str:
        return self.semesterID
    
    def setSemesterID(self,id):
        self.semesterID = id

    def getCourses(self)->list:
        return self.courses
    
    #no setter for courses since its a list. Instead, courses has add and remove course functions
    def addCourse(self,course):
        self.courses.append(course)
        self.semesterDifficulty = self.calculateSemesterDifficulty()
        self.totalCreditHours = self.calculateTotalCreditHours()

    def removeCourse(self,course):
        self.courses.remove(course)
        self.semesterDifficulty = self.calculateSemesterDifficulty()
        self.totalCreditHours = self.calculateTotalCreditHours()

    def getSemesterDifficulty(self)->float:
        return self.semesterDifficulty 

    def getTotalCreditHours(self)->int:
        return self.totalCreditHours
    
    #takes the list of courses and calculates the average difficulty
    #-1 semester difficulty means that none of the courses in the semester have difficulty ratings
    def calculateSemesterDifficulty(self)->float:
        totalDifficulty = 0
        numCourses = 0
        for course in self.courses:
            if(course.getDifficultyRating() != -1.0):
                totalDifficulty += course.getDifficultyRating()
                numCourses += 1
        if numCourses != 0:
            return round(totalDifficulty/numCourses,2)
        else:
            return -1
    
    #takes the list of courses and calculates the totalCreditHours
    def calculateTotalCreditHours(self)->int:
        creditHours = 0
        for course in self.courses:
            creditHours += course.getCreditHours()
        return creditHours