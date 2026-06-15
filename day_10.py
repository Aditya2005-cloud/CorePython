class Student:
    def __init__(self,name,age):#  __init__ is automatically called.
        self.name=name
        self.age=age
a=input("Enter your name: ")
b=int(input("Enter your age: "))
s1=Student(a,b)
print(s1.name)
print(s1.age)
print(s1)  # <__main__.Student object at 0x00000163D3C5D160>