# animal.py
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")
    def make_sound(self):
        print("Animal makes sound")