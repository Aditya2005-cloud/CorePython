#function with default value
def d(a="name"):
    print(f"helow, {a}")
a=input("enter your name: ")
d(a)

def unlimited(*args):#by convention and with no limit. but u can use any name
# Problem
# Suppose you want to pass information like:
# name="Aditya",age=25,country="India"(*args is not designed for that.)
    return args
print(list(unlimited(1,2,3,4,5)))
print(unlimited(1))
print(unlimited(1,2))
print(unlimited(1,2,3))
print(unlimited(1,2,3,4))
print(unlimited(1,2,3,4,5))

def info(**kwargs):#we can use any name 
    #print(type(kwargs)) its return type is dictionary proved by python
    return kwargs
print(info(name="Aditya",age=25,country="India"))

def info1(**hmm):
    for key,value in hmm.items():
        print(f"{key}={value}")
info1(name="Aditya",age=25,country="India")