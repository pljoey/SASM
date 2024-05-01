from CourseController import CourseController
from UserController import UserController

class UserInterface:
    def __init__(self):
        self.course_controller = CourseController.CourseController()
        self.user_controller = UserController.user_controller()

    def start_menu(self):
        valid_input = False
        while not valid_input:
            print("Please choose an option by typing the respective number:")
            print("1. Create an account")
            print("2. Login")
            print("3. Exit")
            response = input()
            match response:
                case "1":
                    self.sign_up()
                case "2":
                    self.login()
                    valid_input = True
                case "3":
                    print("Goodbye!")
                    exit()
                case _:
                    print("not a valid input \n")
            

    def basic_menu(self):
        back = False
        while not back:
            print("Please choose an option by typing the respective number:")
            print("1. Create schedule")
            print("2. View/edit schedule")
            print("3. View course/professor information")
            print("4. View/edit account")
            print("5. Log out")
            response = input()
            match response:
                case "1":
                    self.create_schedule_menu()
                case "2":
                    self.view_schedule_menu()
                case "3":
                    self.view_info_menu()
                case "4":
                    self.account_menu()
                case "5":
                    self.start_menu()
                    back = True
                case _:
                    print("not a valid input \n")

    def sign_up(self):
        print("please sign up")
        pass

    def login(self):
        print("I'm too lazy to implement login right now. Please pretend that you just finished logging in")
        self.basic_menu()

    def create_schedule_menu(self):
        print("menu for creating a schedule")
        print("IDK what is gonna be in this menu yet")

    def view_schedule_menu(self):
        back = False
        while not back:
            print("do you want to view or edit a schedule?")
            print("1. View schedule")
            print("2. Edit schedule")
            print("3. Back")
            response = input()
            match response:
                    case "1":
                        print("viewing schedule")
                    case "2":
                        print("editting schedule")
                    case "3":
                        self.basic_menu()
                    case _:
                        print("not a valid input \n")
        

    def view_info_menu(self):
        back = False
        while not back:
            print("do you want to view course or professor information?")
            print("1. View course information")
            print("2. View professor information")
            print("3. View Remaining courses")
            print("4. Back")
            response = input()
            match response:
                case "1":
                    self.search_for_course()
                case "2":
                    self.search_for_professor()
                case "3":
                    # Left is a str array of all remaining coures. 
                    left = self.view_remaining_course()
                    for x in left:
                        print(left.pop(0))   
                                   
                    back = True
                case "4":
                    self.basic_menu()
                    back = True
                case _:
                    print("not a valid input \n")

    def account_menu(self):
        print("menu for viewing account")

    def search_for_professor(self):
        print("please enter a professor's last name:")
        response = input()
        valid_prof = self.course_controller.get_professor_info(response)

    def search_for_course(self):
        print("please enter a course's id:")
        response = input()
        valid_course = self.course_controller.get_course_info(response)

    def view_remaining_course(self):
        valid_course = self.user_controller.view_remaining_course()

    def get_course_review(self):
        pass

    def save_schedule_to_account(self):
        pass

    def edit_prefences(self):
        pass

    
ui = UserInterface()
ui.start_menu()