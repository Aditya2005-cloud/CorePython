# class car:
#     def properties(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def details(self):
#         print(f"Car brand is {self.brand} the model is {self.model} made in {self.year}")
# s1=car()
# s1.properties("Honda","Civic",2022)
# s1.details()

#better way
class Car:
    def __init__(self, brand, model, year):#   __init__ runs only once
        self.brand = brand
        self.model = model
        self.year = year
    def details(self):# self mean This object
        print(f"Car brand is {self.brand}, model is {self.model}, made in {self.year}")
c1 = Car("Honda", "Civic", 2022)
c1.details()
print(c1.__dict__)#__dict__ shows everything stored inside the object.
print(Car.__dict__)



class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def show_balance(self):
        print(f"Owner is {self.owner} and balance is {self.balance}")
b1=Bank("Aditya",100000)
b1.show_balance()
b1.deposit(1000)
b1.show_balance()
b1.withdraw(5000)
b1.show_balance()