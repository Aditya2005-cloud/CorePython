def greed():
    print("Hellworld")
    return "hello world"
greed()  #print() Displays result.
print("="*20)
print(greed()) #return Sends result back to whoever called the function.

#Function with Parameters
def user(name,age):
    print(f"Hello {name}, you are {age} years old.")
user("Kaka",22)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
user(name,age)

#Function with Return
def add(num1,num2):
    return num1+num2
result=add(10,20)
print(result)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(add(a,b))

#Default Arguments
def greet(name="Guest"):
    print("Hello", name)

