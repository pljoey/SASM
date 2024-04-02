from Course import Course
import Professor

#class for course section
class CourseSection(Course):
    #constructor for CourseSection
    def __init__ (self, ParentCourse, sectionNum, prof = []):
        self.courseID = ParentCourse.getCourseID()    
        self.courseName = ParentCourse.getCourseName()  
        self.creditHours = ParentCourse.getCreditHours()
        self.isElective = ParentCourse.getIsElective()
        self.difficultyRating = ParentCourse.getDifficultyRating(); 
        self.professor = prof
        self.sectionNumber = sectionNum

    #getter and setter for sectionNumber and Professor
    def getSectionNumber(self)->int:
        return self.sectionNumber
    
    def setSectionNumber(self, newSection):
        self.sectionNumber = newSection
    
    def getProfessor(self)->list:
        return self.professor
    
    def setProfessor(self, prof):
        self.professor


    
