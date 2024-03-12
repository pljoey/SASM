import Review

#methods and attributes for the professor class
class Professor:
    #constructor
    def __init__(self, firstName, lastName, prefix = "", professorReviews = []):
        self.firstName = firstName
        self.lastName = lastName
        self.prefix = prefix
        self.professorReviews = professorReviews
        self.score = self.calculateScore()

    #getter and setter functions for all of the attributes
    def getFirstName(self)-> str:
        return self.firstName
    
    def setFirstName(self, name):
        self.firstName = name

    def getLastName(self)-> str:
        return self.lastName
    
    def setLastName(self, name):
        self.lastName = name

    def getPrefix(self)-> str:
        return self.prefix
    
    def setPrefix(self, pre):
        self.prefix = pre
  
    def getProfessorReviews(self) -> list:
        return self.professorReviews

    #no setters for getProfessorRatings since its a list. Instead it has add and remove rating methods
    def addProfessorReview(self, review):
        self.professorReviews.append(review)
        self.score = self.calculateScore()

    def removeProfessorReview(self, review):
        self.professorReviews.remove(review)
        self.score = self.calculateScore()

    #a value of -1.0 for score means that there is no score yet
    def getScore(self)->float:
        return self.score

    def calculateScore(self)->float:
        totalScore = 0
        numReviews = 0
        for review in self.professorReviews:
            totalScore += review.getScore()
            numReviews += 1
        if numReviews == 0:
            return -1.0
        else:
            return totalScore/numReviews

    #gets out all professor information for printing
    def getAllInfo(self)->str:
        if(self.prefix != "" and self.score != -1.0):
            return  self.prefix + " " + self.firstName + " " + self.lastName +  " - Score: " + str(self.score)
        elif(self.prefix != "" and self.score == -1.0):
            return  self.prefix + " " + self.firstName + " " + self.lastName +  " - Score: " + "N/A"
        elif(self.prefix == "" and self.score != -1.0):
            return self.firstName + " " + self.lastName +  " - Rating: " + str(self.score)
        else:
            return  self.firstName + " " + self.lastName +  " - Rating: " + "N/A"
