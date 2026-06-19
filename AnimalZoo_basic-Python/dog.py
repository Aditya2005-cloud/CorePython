# dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def make_sound(self):
        print("Woof")