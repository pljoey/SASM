
#methods and attributes for the professor class
class Professor:
    #constructor
    def __init__(self, first_name, last_name, prefix = "", professor_reviews = [], rating = -1.0, difficulty = -1.0, would_take_again = -1.0):
        self.first_name = first_name
        self.last_name = last_name
        self.prefix = prefix
        self.rating = rating
        self.difficulty = difficulty
        self.would_take_again = would_take_again

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
    
    def get_rating(self)->float:
        return self.rating
    
    def set_rating(self, rating):
        self.rating = rating

    def get_difficulty(self)->float:
        return self.difficulty
    
    def set_difficulty(self, diff):
        self.difficulty = diff

    def get_would_take_again(self)->float:
        return self.would_take_again

    def set_would_take_again(self, would_take_again):
        self.would_take_again = would_take_again
