import User

def sign_up():
    new_user = 0
    username = input("What is your username: ")
    while(False): #check if username already exists
        username = input("Username already exists, try a new username: ")
    password = input("What is your password: ")
    if(input("Do you have any previous courses taken to list? (Y/N) " == "Y")):
        courses_taken = input("What courses have you taken? Insert in a space separated lists, IE: 'IT386 IT383 ...' ")
        courses_taken = courses_taken.split(" ")
        new_user = User(username, password, courses_taken)
    else:
        new_user = User(username, password)
    #add new user into the database


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

def get_choice():
    while(True):
        print("What would you like to do?\n1)Create Schedule\n2)Edit Schedule\n3)Edit Preferences\n4)View Course Information\n5)View Professor Information\n6)Exit")
        choice = input()
        if(choice == "1"):
            pass
        elif(choice == "2"):
            pass
        elif(choice == "3"):
            pass
        elif(choice == "4"):
            pass
        elif(choice == "5"):
            pass
        elif(choice == "6"):
            break
        else:
            print("Incorrect choice")

if __name__ == "__main__":
    start()
    get_choice()