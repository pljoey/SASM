from CourseController import CourseController
import ratemyprofessor
from UserController import UserController

user_controller = UserController()
course_controller = CourseController()
main_loop_string = "What would you like to do?\n1)Create Schedule\n2)Edit Schedule\n3)Edit Preferences\n4)View Course Information\n5)View Professor Information\n6)Exit"
edit_preference_string = "What would you like to do?\n1)Edit Courses taken\n2)Edit BlackList"

def sign_up():
    """
    This function will create a new user and auto log the user in
    the return value is the user
    """ 
    username = input("What is your username: ")
    while(user_controller.find_username(username)): #check if username already exists
        username = input("Username already exists, try a new username: ")
    password = input("What is your password: ")
    if(input("Do you have any previous courses taken to list? (Y/N) ") == "Y"):
        courses_taken = input("What courses have you taken? Insert in a space separated lists, IE: 'IT386 IT383 ...' ")
        courses_taken = courses_taken.split(" ")
        return user_controller.create_user(username, password, courses_taken)
    else:
        return user_controller.create_user(username, password)


def log_in():
    username = input("What is your username: ")
    while(not user_controller.find_username(username)): #check if username not found
        username = input("Username not found, please try again: ")
    password = input("What is the password: ")
    while(not user_controller.check_password(username, password)): #password does not match
        password = input("Password was incorrect for username " + username + ", please try again: or enter '1' for forgot password")
        if (password == "1"):
            password = input("Input new password: ")
            return user_controller.update_password(username, password)
    return user_controller.get_user(username, password)

def start():
    #setup professor information
    professor_list = [] #this is a list of professors that are retrieved from the database so we can update the information using the api
    ratemyprofessor.get_professors_by_school_and_name(ratemyprofessor.get_school_by_name("Illinois State University"), professor_list)
    #update professor information then continue
    choice = input("Would you like to sign up(1) or log in(2)? (1/2)")
    if(choice == "1"):
        return sign_up()
    elif(choice == "2"):
        return log_in()

def edit_preferences(user):
    while(True):
        choice = input(edit_preference_string)
        if(choice == "1"):
            pass
        elif(choice == "2"):
            pass
        else:
            print("Incorrect Choice")

def view_professor_information():
    choice = input("Input professor name: ")
    course_controller.get_professor_info(choice)


if __name__ == "__main__":
    user = start()
    print()
    while(True):
        choice = input(main_loop_string)
        if(choice == "1"): #create schedule
            pass
        elif(choice == "2"): #edit schedule
            pass
        elif(choice == "3"): #Edit preferences
            edit_preferences(user)
        elif(choice == "4"): #view course info
            pass
        elif(choice == "5"): #view professor info
            view_professor_information()
        elif(choice == "6"): #exit
            break
        else:
            print("Incorrect Choice")