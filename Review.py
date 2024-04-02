#methods and attributes for Rating class
class Review:
    #constructor for Rating class
    def __init__ (self, score, description, difficulty = -1.0, course = ""):
        self.score = score
        self.description = description
        self.difficulty = difficulty
        self.courseName = course

    #getters and setters for the above attributes
    def getScore(self)->float:
        return self.score
    
    def setScore(self,score):
        self.score = score

    def getDescription(self)->str:
        return self.description
    
    def setDescription(self, description):
        self.description = description

    def getDifficulty(self)->float:
        return self.difficulty
    
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    def getCourseName(self)->str:
        return self.courseName
    
    def setCourseName(self,course):
        self.courseName = course