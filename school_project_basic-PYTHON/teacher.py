from person import Person as p

class Teacher(p):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        #self.teacher_id = teacher_id
        self.subject = subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

# #test
# t1=Teacher("Alice",20,"Maths")#passes 3 arguments
# t1.introduce()
# t1.teach()