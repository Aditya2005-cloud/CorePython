from animal import Animal as a 

class Cat(a):
    def __init__(self,name,age):
        super().__init__(name,age)
    def meow(self):
        print(f"{self.name} is meowing")  