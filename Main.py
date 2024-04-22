#import CourseController
from Controllers import UserController

user_controller = UserController()
main_loop_string = "What would you like to do?\n1)Create Schedule\n2)Edit Schedule\n3)Edit Preferences\n4)View Course Information\n5)View Professor Information\n6)Exit"
edit_preference_string = "What would you like to do?\n1)Edit Courses taken\n2)Edit BlackList"

def sign_up():
    """
    This function will create a new user and auto log the user in
    the return value is the user
    """ 
    username = input("What is your username: ")
    while(False): #check if username already exists
        username = input("Username already exists, try a new username: ")
    password = input("What is your password: ")
    if(input("Do you have any previous courses taken to list? (Y/N) " == "Y")):
        courses_taken = input("What courses have you taken? Insert in a space separated lists, IE: 'IT386 IT383 ...' ")
        courses_taken = courses_taken.split(" ")
        return user_controller.create_user(username, password, courses_taken)
    else:
        return user_controller.create_user(username, password)


def log_in():
    username = input("What is your username: ")
    while(False): #check if username not found
        username = input("Username not found, please try again: ")
    password = input("What is the password: ")
    while(False): #password does not match
        password = input("Password was incorrect for username " + username + ", please try again: ")

def start():
    choice = input("Would you like to sign up(1) or log in(2)? (1/2)")
    if(choice == "1"):
        sign_up()
    elif(choice == "2"):
        log_in()

def edit_preferences(user):
    while(True):
        choice = input(edit_preference_string)
        if(choice == "1"):
            pass
        elif(choice == "2"):
            pass
        else:
            print("Incorrect Choice")

if __name__ == "__main__":
    user = start()
    while(True):
        choice = input(main_loop_string)
        if(choice == "1"):
            pass
        elif(choice == "2"):
            pass
        elif(choice == "3"):
            edit_preferences(user)
        elif(choice == "4"):
            pass
        elif(choice == "5"):
            pass
        elif(choice == "6"):
            break
        else:
            print("Incorrect Choice")