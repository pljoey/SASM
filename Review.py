#methods and attributes for Rating class
class Review:
    #constructor for Rating class
    def __init__ (self, score, description):
        self.score = score
        self.description = description

    #getters and setters for the above attributes
    def getScore(self)->float:
        return self.score
    
    def setScore(self,score):
        self.score = score

    def getDescription(self)->str:
        return self.description
    
    def setDescription(self, description):
        self.description = description