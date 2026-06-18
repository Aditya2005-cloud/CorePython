from person import Person as p

# class Student(p):
#     def __init(self,student_id):#name and age are undefined
#         #super() is a built-in Python function used to access methods and attributes from a parent (base) class.
#         #means: "Call the __init__() method from the parent class (Person) and initialize name and age."
#         self.student_id=student_id
#     def student_study(self):
#         print(f"{self.name} is studying")

# #test
# s1=Student("Alice",20,"12345")#Student("Alice",20,"12345") passes 3 arguments
# s1.introduce()
# s1.student_study() {not working as name and age are undefined}

class Student(p):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)# Call Person constructor
        self.student_id = student_id
    def student_study(self):
        print(f"{self.name} is studying")

# #test
# s1=Student("Alice",20,"12345")#Student("Alice",20,"12345") passes 3 arguments
# s1.introduce()
# s1.student_study()  working