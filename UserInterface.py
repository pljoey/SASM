import CourseController
import UserController
import ratemyprofessor

class UserInterface:
    def __init__(self):
        self.course_controller = CourseController.CourseController()
        self.user_controller = UserController.UserController()

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
                    self.logout()
                    self.start_menu()
                    back = True
                case _:
                    print("not a valid input \n")

    def sign_up(self):
        user_created = False

        while not user_created:
            print("Please enter a username:")
            username = input()
            print("Please enter a password:")
            password = input()

            user_created = self.user_controller.create_user(username, password)

            if not user_created:
                print("A user with that Username already exists, please enter a new username")

        print('User Created \n')

    def forgot_password(self, username):
        password = input("What is your new password? ")
        self.user_controller.update_password(username, password)

    def login(self):
        logged_in = False

        while not logged_in:
            print("Please input your username:")
            username = input()
            print("Please enter your password:")
            password = input()

            logged_in = self.user_controller.login(username, password)

            if not logged_in:
                print("Incorrect username or password, press 1) to try again or 2) forgot password \n") 
                choice = input()
                if (choice == "2"):
                    self.forgot_password(username)
        
        self.basic_menu()

    def logout(self):
        print('User Logged Out')
        self.user_controller.logout()
    
    def delete_user(self):
        print('All data associated with your account will be deleted. Are you sure you want to delete your account?')
        print('If so, please enter your password')
        password = input()

        if self.user_controller.delete_user(password):
            print('Account deleted \n')
            self.start_menu()
        else:
            print('Account not deleted')

    def fill_schedule(self):
        self.user_controller.fill_schedule()

    def view_schedule(self):
        self.user_controller.view_schedule()

    def create_schedule_menu(self):
        success = self.user_controller.create_schedule()
        if success == True:
            self.fill_schedule()
        else:
            print("Schedule currently in use, please save or delete the schedule to create a new one")

    def view_schedule_menu(self):
        back = False
        while not back:
            print("do you want to view or edit a schedule?")
            print("1. View schedule")
            print("2. Edit schedule")
            print("3. Save Schedule")
            print("4. Load Schedule")
            print("5. Export Schedule to Text file")
            print("6. create custom course")
            print("7. Back")
            response = input()
            match response:
                    case "1":
                        self.view_schedule()
                    case "2":
                        self.schedule_edit_menu()
                    case "3":
                        self.save_schedule_to_account()
                    case "4":
                        self.load_schedule()
                    case "5":
                        self.export_to_format()
                    case "6":
                        self.create_custom_course_menu()
                    case "7":
                        self.basic_menu()
                    case _:
                        print("not a valid input \n")
        
    def schedule_edit_menu(self):
        back = False
        while not back:
            print("please choose an option:")
            print("1. Add course")
            print("2. Remove course")
            print("3. Delete Schedule")
            print("4. Back")
            response = input()
            match response:
                    case "1":
                        self.add_course_menu()
                    case "2":
                        self.user_controller.remove_course()
                    case "3":
                        if self.user_controller.delete_schedule():
                            print("Schedule successfully deleted")
                        else:
                            print("Schedule could not be deleted")
                    case "4":
                        self.view_schedule_menu()
                        back = True
                    case _:
                        print("not a valid input \n")

    def view_info_menu(self):
        back = False
        while not back:
            print("What information would you like to view?")
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
                    print("Here are the remaining core courses for your major: ")
                    list = self.user_controller.view_remaining_courses()
                    y = 0
                    for x in list:
                        print(x," ", end='')
                        y = y + 1
                        if y == 3:
                            print()
                            y = 0                
                case "4":
                    self.basic_menu()
                    back = True
                case _:
                    print("not a valid input \n")

    def account_menu(self):
        back = False
        while not back:
            print("do you want to view course or professor information?")
            print("1. View account information")
            print("2. edit prior courses")
            print("3. edit preferences")
            print("4. Delete Account")
            print("5. back")
            response = input()
            match response:
                case "1":
                    self.view_account()
                case "2":
                    print("1. Add prior courses")
                    print("2. Remove prior courses")
                    print("3. Back")
                    response = input()
                    match response:
                        case "1":
                            cont = "y"
                            while cont ==  "y":
                                print("Enter the name of a course: ")
                                course = input()
                                worked = self.user_controller.add_previous_courses(course)
                                if worked:
                                    print("Course added, add more (y/n): ")
                                    cont = input()
                                else:
                                    print("Course not added, try more (y/n): ")
                                    cont = input()
                        case "2":
                            cont = "y"
                            while cont ==  "y":
                                print("Enter the name of a course: ")
                                course = input()
                                worked = self.user_controller.remove_previous_course(course)
                                if worked:
                                    print("Course removed, remove more (y/n): ")
                                    cont = input()
                                else:
                                    print("Course not removed, remove more (y/n): ")
                                    cont = input()
                        case "3":
                            self.basic_menu()
                            back = True
                        case _:
                            print("not a valid input \n")
                case "3":
                    self.course_controller.edit_preferences()
                case "4":
                    #TODO: Fix going between start_menu and basic_menu
                    self.delete_user()
                case "5":
                    self.basic_menu()
                    back = True
                case _:
                    print("not a valid input \n")

    def search_for_professor(self):
        print("please enter a professor's last name:")
        response = input()
        valid_prof = self.course_controller.get_professor_info(response)
        if(valid_prof):
            print(response)
            print("Overall rating: " + str(ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("Illinois State University"), response).rating))
            print("Difficulty rating: " + str(ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("Illinois State University"), response).difficulty))
            print("Would take again: " + str(ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("Illinois State University"), response).would_take_again) + "%")

    def search_for_course(self):
        print("please enter a course's id:")
        response = input()
        valid_course = self.course_controller.get_course_info(response)

    def add_course_menu(self):
        print("please enter a course's department:")
        dept = input()
        print("please enter a course's id number:")
        id = input()
        print(self.user_controller.add_course(dept, id))

    def create_custom_course_menu(self):
        print("please enter a name for the course")
        name = input()
        print("please enter the start time in the form hh:mm a/p")
        start_time = input()
        print("please enter the end time in the form hh:mm a/p")
        end_time = input()
        self.course_controller
        print("Please enter the days that the course is on in the format M/Tu/W/Th/F/")
        days = input()
        self.course_controller.add_custom_course(name,start_time,end_time,days)

    def get_course_review(self):
        pass

    def save_schedule_to_account(self):
        self.user_controller.save_schedule()

    def load_schedule(self):
        pass

    def edit_prefences(self):
        pass

    def export_to_format(self):
        self.user_controller.export_to_format()

    
ui = UserInterface()
ui.start_menu()