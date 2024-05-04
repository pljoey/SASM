import Course
import ExportableFormatFactory
import Preferences
import Schedule
from DatabaseManagementFactory import DatabaseManagementFactory
import hashlib
import random

class CourseHandler:
    #method for the user to manually create a course 
    def __init__(self):
       self.database = DatabaseManagementFactory.get_database_instance('mariadb')


    def create_course(course_name, course_time, section):
        pass

    #
    def get_course_section_review(section):
        return
    
    def add_custom_course(self,name,start_time,end_time,days)->bool:
        id = random.randrange(start = 100, stop = 999)
        day_list = [False,False,False,False,False]
        department = "CUS"
        while self.database.check_for_course("CUS", id) == True:
            id += 1
            if id == 1000:
                id = 100
        custom = Course.Course(id, name, 0, True)
        #getting the days the custom course is on
        cur_str = ""
        for char in days:
            if char != '/':
                cur_str += char
            else:
                match cur_str:
                    case "M":
                        day_list[0] = True
                    case "Tu":
                        day_list[1] = True
                    case "W":
                        day_list[2] = True
                    case "Th":
                        day_list[3] = True
                    case "F":
                        day_list[4] = True
                    case _:
                        print("invalid day format. Unable to make custom course")
                        return False
                cur_str = ""

        #converting start time to readable format
        start_time_float = 0.0
        cur_num = ""
        for char in start_time:
            if(char.isnumeric):
                cur_num += char
            elif char == ':':
                start_time_float += int(cur_num)
                cur_num = ""
            elif char == ' ':
                start_time_float += (int(cur_num)/100)
            elif char == 'p':
                start_time_float += 12
            elif char != 'a':
                print("invalid start time format. Unable to make custom course")
                return False
        
        #converting end time to readable format
        end_time_float = 0.0
        cur_num = ""
        for char in end_time:
            if(char.isnumeric):
                cur_num += char
            elif char == ':':
                end_time_float += int(cur_num)
                cur_num = ""
            elif char == ' ':
                end_time_float += (int(cur_num)/100)
            elif char == 'p':
                end_time_float += 12
            elif char != 'a':
                print("invalid start time format. Unable to make custom course")
                return False

        custom.add_section(1, None, start_time_float, end_time_float, day_list[0],day_list[1],day_list[2],day_list[3],day_list[4])
        self.database.add_course(department, id, name)
        self.database.add_section(1, "Custom", "Course", "CUS", "CUS", id, start_time_float, end_time_float, day_list[0],day_list[1],day_list[2],day_list[3],day_list[4])
        return True

