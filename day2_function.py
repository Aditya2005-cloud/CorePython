# practice functions

def hello():
    print("Hello, World!")
    return #this ends the function and returns None by default
    print("This will never be printed because it's after the return statement.")
hello() # This will call the function and print "Hello, World!" to the console


def greet(name="no name given",age=0):# name and age are parameters with default values
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)# Alice and 30 are passed as arguments to the function
greet("Bob")  # age will use default value 0
greet()  # both name and age will use default values


def value(number):
    number = 42
    print(f"Inside the function, number is {number}")
num = 10
value(num)
print(num)  # This will print 10, not 42, because the function does not modify the original variable outside its scope


def name(value):
    value["name"] = "nothing"

val = {"name": "satyarth"}
name(val)
print(val)  # This will print {'name': 'nothing'} because the function modifies the dictionary passed as an argument, demonstrating that mutable objects can be modified within a function. 


def hello1(a):
    if a==True:
        return "end"
    print("hello")
hello1("Alice")# This will call the function with "Alice" as an argument, but since "Alice" is not equal to True, it will print "hello" and return None.
hello1(True) # This will call the function with True as an argument, which will return "end" and not print anything because the function exits before reaching the print statement.


def hello2(a):
    if not a:
        return "end"
    print("hello "+ str(a) )# or print("hello", a)
hello2("Alice")# This will call the function with "Alice" as an argument, which will print "hello" and return None because "Alice" is considered truthy.
hello2(False) # This will call the function with False as an argument, which will return "end" because False is considered falsy in Python.
hello2("") # This will call the function with an empty string as an argument, which will also return "end" because an empty string is considered falsy in Python.
hello2(None) # This will call the function with None as an argument, which will also return "end" because None is considered falsy in Python.
hello2(0) # This will call the function with 0 as an argument, which will also return "end" because 0 is considered falsy in Python.
hello2(True) # This will call the function with True as an argument, which will print "hello True" and return None because True is considered truthy in Python.


age = 25 # global variable
def check_age():
    age = 30 # local variable
    print(f"Inside the function, age is {age}")
check_age() # This will call the function and print "Inside the function, age is 30" because the local variable age inside the function shadows the global variable age.
print(f"Outside the function, age is {age}") # This will print "Outside the function, age is 25" because the global variable age is not affected by the local variable inside the function.


def hee(a):
    def inner_hee(b):
        print("inner hee", b)
    print("hee",a)
hee(10) # This will call the function hee with 10 as an argument, which will print "hee 10" but will not call the inner function inner_hee, so "inner hee" will not be printed.
inner_hee(20) # This will raise a NameError because inner_hee is defined inside the function hee and is not accessible outside of it.   


def talk(word):
    def inner_talk():
        nonlocal word # This allows us to modify the variable 'word' defined in the outer function 'talk'
        print("inner talk", word)
    print("talk", word)
    inner_talk() # This will call the inner function inner_talk, which will print "inner talk" followed by the value of 'word'
talk("hello") # This will call the function talk with "hello" as an argument, which will print "talk hello" and then "inner talk hello" because the inner function inner_talk accesses the nonlocal variable 'word' from the outer function.


