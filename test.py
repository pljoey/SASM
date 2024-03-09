import Professor
import Course
import Schedule
import Semester
import User
import Preferences
import Blacklist
import Review

#code used for testing review class
JohnReview1 = Review.Review(3.5, "John was alright I guess")
JohnReview2 = Review.Review(0.0, "I hate John")
JaneReview1 = Review.Review(5.0, "Jane is the greatest teacher of all time")

#code used for testing professor class
John = Professor.Professor("John", "Doe", "Dr.", [JaneReview1,JohnReview2])
Jane = Professor.Professor("Jane", "Doe")
print(John.getAllInfo())
John.setPrefix("")
print(John.getAllInfo())
print(Jane.getAllInfo())
Jane.setPrefix("Dr.")
Jane.addProfessorReview(JaneReview1)
print(Jane.getAllInfo())

#code for testing course class
RishiReview1 = Review.Review(4.3, "Rishi was great")
Rishi = Professor.Professor("Rishi", "Saripalle","",[RishiReview1])
IT326 = Course.Course("IT326", "Principles of Software Engineering", 3, False, 5.0,[Rishi])
print(IT326.getCourseID() + " " + IT326.getCourseName())
IT326.addProfessor(John)
IT326.addProfessor(Jane)
for professor in IT326.getProfessors():
    print(professor.getAllInfo())
IT326.removeProfessor(Rishi)
for professor in IT326.getProfessors():
    print(professor.getAllInfo())


#code for testing the semester class
IT101 = Course.Course("IT101", "Coding or Something IDK", 1, False, 3.5,[Jane])
ECO325 = Course.Course("ECO325", "The Economy I Guess", 5, True, 1.0, [John])
BIO276 = Course.Course("BIO276", "The Mitochondria and You", 3, False, 4.3, [Rishi])
Fall2024 = Semester.Semester("Fall2024",[IT326,IT101,ECO325])
print("Difficulty: " + str(Fall2024.getSemesterDifficulty()) + " Total Credit Hours: " + str(Fall2024.getTotalCreditHours()))
Fall2024.addCourse(BIO276)
Fall2024.removeCourse(IT326)
print("Difficulty: " + str(Fall2024.getSemesterDifficulty()) + " Total Credit Hours: " + str(Fall2024.getTotalCreditHours()))
for course in Fall2024.getCourses():
    print(course.getCourseID())

#code used for testing the schedule class
Winter2025 = Semester.Semester("Winter2025",[BIO276,ECO325])
Winter2024 = Semester.Semester("Winter2024", [IT326, IT101])
firstSchedule= Schedule.Schedule()
print(firstSchedule.getScheduleType())
firstSchedule.addSemester(Winter2024)
print(firstSchedule.getScheduleType())
firstSchedule.addSemester(Fall2024)
firstSchedule.addSemester(Winter2025)
firstSchedule.removeSemester(Winter2024)
print(firstSchedule.getScheduleType())
for semester in firstSchedule.getSemesters():
    print(semester.getSemesterID())

#code used for testing the blacklist class
myBlacklist = Blacklist.Blacklist()
myBlacklist.addToBlacklist(IT101)
myBlacklist.addToBlacklist(BIO276)
myBlacklist.addToBlacklist(John)
myBlacklist.addToBlacklist(Jane)
for item in myBlacklist.getBlacklist():
    if(isinstance(item,Professor.Professor)):
        print(item.getFirstName())
    elif(isinstance(item,Course.Course)):
        print(item.getCourseID())
    else:
        print("What?")

#code for testing the Preferences class
myPreferences = Preferences.Preferences(12, [ECO325])
myPreferences.addElective(BIO276)
myPreferences.removeElective(ECO325)
myPreferences.addBlacklistedItems([BIO276,ECO325,Rishi,John,Jane])
for elective in myPreferences.getPreferredElectives():
    print(elective.getCourseName())
for item in myPreferences.getLocalBlacklist().getBlacklist():
    if(isinstance(item,Professor.Professor)):
        print(item.getFirstName())
    elif(isinstance(item,Course.Course)):
        print(item.getCourseID())
    else:
        print("What?")
myPreferences.removeBlacklistedItems([ECO325,Rishi])
for item in myPreferences.getLocalBlacklist().getBlacklist():
    if(isinstance(item,Professor.Professor)):
        print(item.getFirstName())
    elif(isinstance(item,Course.Course)):
        print(item.getCourseID())
    else:
        print("What?")

#code for testing user class
newUser = User.User("ItsMe", 1,[ECO325],[firstSchedule],[myPreferences])
print(newUser.getUserName() + " " + str(newUser.getUserID()))
newUser.addCourse(IT101)
for course in newUser.getCoursesTaken():
    print(course.getCourseID())