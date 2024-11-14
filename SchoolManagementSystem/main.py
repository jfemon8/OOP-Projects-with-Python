from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

school = School("ABC School", "Barishal")

eight = Classroom("eight")
nine = Classroom("nine")
ten = Classroom("ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim", eight)
karim = Student("Karim", eight)
selim = Student("Selim", nine)
akbor = Student("Akbor", nine)
shikder = Student("Shikder", ten)
rasul = Student("Rasul", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(selim)
school.student_admission(akbor)
school.student_admission(shikder)
school.student_admission(rasul)

emon = Teacher("Emon")
anik = Teacher("Anik")
minha = Teacher("Minha")

bangla = Subject("Bangla", minha)
english = Subject("English", anik)
math = Subject("Math", emon)

school.add_teacher(bangla, minha)
school.add_teacher(english, anik)
school.add_teacher(math, emon)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)
nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(math)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)

eight.semester_final()
nine.semester_final()
ten.semester_final()

print(school)
