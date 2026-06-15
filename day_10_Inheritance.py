class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def bark(self):
        print("Woof")
d=Dog()
d.speak()
d.bark()

#Polymorphism
class Dog:
    def sound(self):
        print("Woof")
class Cat:
    def sound(self):
        print("Meow")
#both have sound method but different implementation
d=Dog()
d.sound()
c=Cat()
c.sound()

class MathUtils:
    def __init__(self, calculation_name):
        self.calculation_name = calculation_name  # Instance attribute

    @staticmethod
    def add(x, y):
        # No access to 'self' or 'cls'
        return x + y

# 1. Call directly using the class name (No instantiation required)
result_class = MathUtils.add(5, 10)
print(result_class)  # Output: 15

# 2. Can also be called via an instance
utils = MathUtils("Addition")
result_instance = utils.add(3, 7)
print(result_instance)  # Output: 10

# This is called name mangling.
# Python changes it internally.don't directly access this variable from outside.
class Bank:
    def __init__(self,balance):
        self.__balance = balance
b=Bank(1000)
print(b._Bank__balance)
#better way
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def show_balance(self):
        return self.__balance
b = Bank(1000)
print(b.show_balance())

#insted of self we can use cls
class Student:
    school = "ABC School"
    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school()