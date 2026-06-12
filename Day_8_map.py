#The Syntax of map(function, iterable)
#map() applies a function to every element of an iterable and returns a map object containing the results.
def add_one(x):
    return x+1
a=[1,2,3,4,5,6,7,8,9]
b=map(add_one,a)
print(list(b))
print(map(add_one,a))#This creates a new map object and prints it directly.