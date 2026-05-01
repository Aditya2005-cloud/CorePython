# def about():
#     name=input("Enter your name: ")
#     age=int(input("Enter your age: "))
#     print(f"Hello, {name}! You are {age} years old.")
# about()# This will call the about function, prompting the user for their name and age, and then print a greeting message with that information.

# function with parameters and return statement
name=input("Enter your name: ")
age=int(input("Enter your age: "))
def about(name, age):
    return (f"Hello, {name}! You are {age} years old.");

if age < 18:
    print(about(name, age)+" and you are eligible to vote.")
else:
    print(about(name, age)+" and you are not eligible to vote.")