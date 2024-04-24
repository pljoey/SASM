class UserInterface:

    def start_menu():
        valid_input = False
        while not valid_input:
            print("Please choose an option by typing the respective number:")
            print("1. Create an account")
            print("2. Login")
            print("3. Exit")
            response = input()
            match response:
                case "1":
                    UserInterface.sign_up()
                    valid_input = True
                case "2":
                    UserInterface.login()
                    valid_input = True
                case "3":
                    print("Goodbye!")
                    exit()
                case _:
                    print("not a valid input \n")
            

    def basic_menu():
        valid_input = False
        while not valid_input:
            print("Please choose an option by typing the respective number:")
            print("1. Create schedule")
            print("2. View/edit schedule")
            print("3. View course/professor information")
            print("4. View/edit account")
            print("5. Log out")
            response = input()
            match response:
                case "1":
                    UserInterface.create_schedule_menu()
                    valid_input = True
                case "2":
                    UserInterface.view_schedule_menu()
                    valid_input = True
                case "3":
                    UserInterface.view_info_menu()
                    valid_input = True
                case "4":
                    UserInterface.account_menu()
                    valid_input = True
                case "5":
                    UserInterface.start_menu()
                    valid_input = True
                case _:
                    print("not a valid input \n")

    def sign_up():
        print("please sign up")
        pass

    def login():
        print("I'm too lazy to implement login right now. Please pretend that you just finished logging in")
        UserInterface.basic_menu()

    def create_schedule_menu():
        print("menu for creating a schedule")
        print("IDK what is gonna be in this menu yet")

    def view_schedule_menu():
        print("menu for viewing schedule")

    def view_info_menu():
        print("menu for viewing course and professor information")

    def account_menu():
        print("menu for viewing account")

    def get_course_review():
        pass

    def save_schedule_to_account():
        pass

    def edit_prefences():
        pass

    

UserInterface.start_menu()