from UserHandler import UserHandler

class UserController:
    def __init__(self):
        self.handler = UserController()

    def create_user(username, password):
        return UserHandler.create_user(username, password)

    def login(username, password):
        return UserHandler.login(username, password)

    def logout():
        UserHandler.logout()

    def delete_user():
        UserHandler.delete_user()

    def edit_user_preferences():
        # pass to user handler which passes to user which goes to preferences 
        pass

    def save_schedule_to_database():
        # just pass to user handler
        pass

    def create_schedule():
        # pass to user handler
        pass

    def view_remaining_courses(self):
        return self.handler.view_remaining_courses()
    
    def add_previous_courses(self,course):
        self.handler.add_previous_courses(course)
