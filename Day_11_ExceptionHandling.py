# Exception Handling Roadmap
#  try
#  except specific errors
#  else
#  finally
#  raise
#  custom exceptions

a = 10
b = 0
# print(a / b)#ZeroDivisionError: division by zero

#this is normal try-except block
try:#if there is an exception, it will be handled in the except block
    print(a / b)
except:
    print("You can't divide by zero")

#this is a try-except block with specific error handling
try:#one try block can have multiple except blocks
    print(a / b)
except ZeroDivisionError:
    print("You can't divide by zero")
except SyntaxError:
    print("there is an syntax error")
except NameError:
    print("there is an name error")

#this is a try-except block with else block
try:
    print(a / b)
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("No error")
#checking else block is working
try:
    print(a / 2)
except SyntaxError:
    print("there is an syntax error")
else:#Run this code ONLY IF there was NO error.
    print("else block is working")

print("-"*20)
#using Finally block
try:
    print(a / 2)
except SyntaxError:
    print("there is an syntax error")
finally:#This code always runs.Even if:Error happens or No error happens
    print("finally block is working")

#raise means: YOU create an error yourself.
# password = "123"
# if len(password) < 8:
#     raise ValueError("Password too short")# this will show ur message in the error

print("-"*20)
#Custom Exceptions
#there was no MyError exception so i created my own exception and now it is working
class MyError(Exception):#Exception is a base class for all exceptions(parent class)
    pass
a=10
b=-1
if a<0:
    raise MyError("Age cannot be negative")
else:
    print("Age is valid")
# tested it out and its working
if b<0:
    raise MyError("Age cannot be negative")#this will show ur message in the error
else:
    print("Age is valid")

#now on we will use try catch final block to handle all errors at once in our codes