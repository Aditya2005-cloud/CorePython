#A lambda is an anonymous function.
#Lambda Functions
# def square(x):
#     return x * x (this is a normal function)
square =lambda x: x * x
print(square(5))
add= lambda a,b:a+b
print(add(5,10))

#Lambda Syntax:
#   lambda arguments: expression
#Useful when:
#   Function is small
#   Used only once
#   Passed as an argument to another function
