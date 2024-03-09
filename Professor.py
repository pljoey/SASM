#methods and attributes for the professor class

class Professor:
    #constructor
    def __init__(self, firstName, lastName, prefix = "", professorRating=-1):
        self.firstName = firstName
        self.lastName = lastName
        self.prefix = prefix
        self.professorRating = professorRating

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

    #a value of -1.0 for professorRating means that there is no professorRating rating yet
    def getProfessorRating(self) -> float:
        return self.professorRating

    def setProfessorRating(self, rating):
        self.professorRating = rating
    
    #gets out all professor information for printing
    def getAllInfo(self)->str:
        if(self.prefix != "" and self.professorRating != -1.0):
            return  self.prefix + " " + self.firstName + " " + self.lastName +  " - Rating: " + str(self.professorRating)
        elif(self.prefix != "" and self.professorRating == -1.0):
            return  self.prefix + " " + self.firstName + " " + self.lastName +  " - Rating: " + "N/A"
        elif(self.prefix == "" and self.professorRating != -1.0):
            return self.firstName + " " + self.lastName +  " - Rating: " + str(self.professorRating)
        else:
            return  self.firstName + " " + self.lastName +  " - Rating: " + "N/A"


