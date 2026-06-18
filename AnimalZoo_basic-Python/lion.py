from animal import Animal as a 

class Lion(a):
    def __init__(self,name,age):
        super().__init__(name,age)
    def roar(self):
        print(f"{self.name} is roaring")  