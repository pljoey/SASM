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

    def export(self, schedule: Schedule):
        text_file = open('ScheduleFile', 'w')

        self.schedule = schedule

        courses = schedule.get_courses()

        for course in courses:
            text_file.write(course + '\n')