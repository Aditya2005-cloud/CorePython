from student import Student
from teacher import Teacher

# Create a student
s1 = Student("Alice", 20, "12345")

# Create a teacher
t1 = Teacher("Bob", 35, "Math")

# Use student methods
s1.introduce()
s1.student_study()

print()

# Use teacher methods
t1.introduce()
t1.teach()