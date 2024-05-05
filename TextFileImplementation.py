from FormatAbstract import FormatAbstract
from Schedule import Schedule

class TextFileImplementation(FormatAbstract):
    _instance = None

    def __init__(self):
        self.schedule = None

    @staticmethod
    def get_instance():
        if TextFileImplementation._instance == None:
            TextFileImplementation._instance = TextFileImplementation()

        return TextFileImplementation._instance

    #TODO: Add logic to this function, and figure out how to get the schedule object
    def export(self, schedule: Schedule):
        self.schedule = schedule

        courses = schedule.get_courses()

        for course in courses:
            print(course)
            pass