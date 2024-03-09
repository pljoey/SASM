import Professor
import Course
import Schedule
import Semester
import User
import Preferences

#code used for testing professor class
John = Professor.Professor("John", "Doe", "Dr.", 5.0)
print(John.getAllInfo())
John.setPrefix("")
print(John.getAllInfo())

Jane = Professor.Professor("Jane", "Doe")
print(Jane.getAllInfo())
Jane.setPrefix("Dr.")
print(Jane.getAllInfo())

#code for testing course class
Rishi = Professor.Professor("Rishi", "Saripalle")
IT326 = Course.Course("IT326", "Principles of Software Engineering", 3, False, [Rishi], 5.0)
print(IT326.getCourseID() + " " + IT326.getCourseName())
IT326.addProfessor(John)
IT326.addProfessor(Jane)
for professor in IT326.getProfessors():
    IT326.getProfessors().getAllInfo()
