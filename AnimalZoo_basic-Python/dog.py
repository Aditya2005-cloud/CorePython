from animal import Animal as a 

class Dog(a):
    def __init__(self,name,age):
        super().__init__(name,age)
    def bark(self):
        print(f"{self.name} is barking")    