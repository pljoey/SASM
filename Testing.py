from UserController import UserController

user = UserController.UserController()


# Tests create user -> Should return true if in database, false otherwise
print(user.create_user("admin","pass"))
# Tests login -> Should return true if login works
print(user.login("admin","pass"))

# Tests view remaining courses - > Should print "[]"
print(user.view_remaining_courses())

# Tests view prior courses - > Should print "[]"
print(user.view_prior_courses())

# Tests add prior courses  - > Should print "True", and then "[IT 326]"
print(user.add_previous_courses("IT 326"))
print(user.view_prior_courses())

# Tests remove prior couress - > Should print "True", then "[]"
print(user.remove_previous_course("IT 326"))
print(user.view_prior_courses())

# Tests log out - > Should print "True" 
print(user.logout())

# Tests delete user 