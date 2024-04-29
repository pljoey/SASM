import Review

#methods and attributes for the professor class
class Professor:
    #constructor
    def __init__(self, first_name, last_name, prefix = "", professor_reviews = [], score = -1.0):
        self.first_name = first_name
        self.last_name = last_name
        self.prefix = prefix
        self.professor_reviews = professor_reviews
        self.score = score

    #getter and setter functions for all of the attributes
    def get_first_name(self)-> str:
        return self.first_name
    
    def set_first_name(self, name):
        self.first_name = name

    def get_last_name(self)-> str:
        return self.last_name
    
    def set_last_name(self, name):
        self.last_name = name

    def get_prefix(self)-> str:
        return self.prefix
    
    def set_prefix(self, pre):
        self.prefix = pre
  
    def get_professor_reviews(self) -> list:
        return self.professor_reviews

    def set_professor_reviews(self,reviews):
        professorReviews = reviews

    
    #a value of -1.0 for score means that there is no score yet
    def get_score(self)->float:
        return self.score
    
    def set_score(self, score):
        self.score = score

