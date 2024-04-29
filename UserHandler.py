import User
#import exportableFormatHandler
import Schedule
import DatabaseManagementHandler

class UserHandler:
    def __init__(self):
        self.aUser
        self.aSched
        self.aData
        pass
                 
    def create_user(self):
        name = input("Username:\n")
        password = input("Password:\n")
        self.aUser = User.User(name,password)
        print("User made.\n")
        pass

    def edit_user_preferences(self):
        self.aUser.set_preferences()
        pass

    def create_schedule(self):
        #We should pass a 
        pass

    def edit_schedule(self):
        pass

    def save_schedule_to_database(self):
        pass

    def save_schedule_to_exportable_format(self):
        pass