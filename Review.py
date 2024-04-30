#methods and attributes for Rating class
class Review:
    #constructor for Rating class
    def __init__ (self, score, description, difficulty = -1.0, course = ""):
        self.score = score
        self.description = description
        self.difficulty = difficulty
        self.course_name = course

    #getters and setters for the above attributes
    def get_score(self)->float:
        return self.score
    
    def set_score(self,score):
        self.score = score

    def get_description(self)->str:
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_difficulty(self)->float:
        return self.difficulty
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_course_name(self)->str:
        return self.course_name
    
    def set_course_name(self,course):
        self.course_name = course