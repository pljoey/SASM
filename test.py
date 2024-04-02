import Professor
import Course
import CourseSection
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
John = Professor.Professor("John", "Doe", "Dr.", [JaneReview1,JohnReview2])
Jane = Professor.Professor("Jane", "Doe")
RishiReview1 = Review.Review(4.3, "Rishi was great")
Rishi = Professor.Professor("Rishi", "Saripalle","",[RishiReview1])
IT326 = Course.Course("IT326", "Principles of Software Engineering", 3, False, 5.0)
IT101 = Course.Course("IT101", "Coding or Something IDK", 1, False, 3.5)
ECO325 = Course.Course("ECO325", "The Economy I Guess", 5, True, 1.0)
BIO276 = Course.Course("BIO276", "The Mitochondria and You", 3, False, 4.3)
IT326Sec1 = CourseSection.CourseSection(IT326,1,[Rishi])
IT101Sec1 = CourseSection.CourseSection(IT101, 1, [Jane])
ECO325Sec1 = CourseSection.CourseSection(ECO325, 1, [John])
BIO276Sec1 = CourseSection.CourseSection(BIO276,1,[John])
Fall2024 = Semester.Semester("Fall2024",[IT326Sec1,IT101Sec1,ECO325Sec1])
Winter2025 = Semester.Semester("Winter2025",[BIO276Sec1,ECO325Sec1])
Winter2024 = Semester.Semester("Winter2024", [IT326Sec1, IT101Sec1])
firstSchedule= Schedule.Schedule()
myBlacklist = Blacklist.Blacklist()
myPreferences = Preferences.Preferences(12, [ECO325])
newUser = User.User("ItsMe", 1,[ECO325],[firstSchedule],[myPreferences])

print(IT101Sec1.getCourseName())
print(IT101Sec1.getSectionNumber())
