def add(a,b):
    return a+b 
a = 10
b = 20
print(add(a,b))

def add_1(a,b):
    print(a+b)
add_1(a,b)

result = add(10, 20)
print(result)   # 30
print(result * 2)  # 60 ✅ works

result = add_1(10, 20)
print(result)   # None ❌
# thats y we should use return when we want to use the result of a function outside of it, and use print when we just want to display the result within the function.

#Function to check even/odd
def check_even_odd(num):
    try:# this is a try block to catch any ValueError that may occur when trying to convert the input to an integer, such as if the user enters a non-numeric value. If a ValueError occurs, it will return a message asking the user to enter a valid integer instead of crashing the program.
        num=int(num)
        if num%2==0:
            return f"{num} is an even number"
        else:
            return f"{num} is an odd number"
    except ValueError:# this except block will catch the ValueError that occurs when the input cannot be converted to an integer, and it will return a message asking the user to enter a valid integer instead of crashing the program.
        return "Please enter a valid integer"
num=input("enter a number: ")
print(check_even_odd(num))

#Function to find largest of 3 numbers
def largest_of_three(num1,num2,num3):
    if num1>num2 and num1>num3:
        return f"{num1} is the largest number"
    elif num2>num1 and num2>num3:
        return f"{num2} is the largest number"
    else:    
        return f"{num3} is the largest number"
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
print(largest_of_three(num1,num2,num3))    


# Function for Student Pass/Fail System
# . Take marks as input
# .Return "Pass" or "Fail"
def student_pass_fail(marks):
    if marks<=30:
        return "Fail"
    else:
        return "Pass"
marks=int(input("enter the marks: "))
print(student_pass_fail(marks))

student={"s1":{"name":"Alice","marks":85},
        "s2":{"name":"Bob","marks":72},
        "s3":{"name":"Charlie","marks":20}}

for s in student.values():
    result=student_pass_fail(s["marks"])
    print(f"{s['name']} has {result} in the exam with marks {s['marks']}")
# ________________________or________________________
for s in student:
    result=student_pass_fail(student[s]["marks"])
    print(f"{student[s]['name']} has {result} in the exam with marks {student[s]['marks']}")


# MINI PROJECT (Calculator)
def calcu(num1 ,num2,what_to_do):
    if what_to_do=="add":
        return num1+num2
    elif what_to_do=="subtract":
        return num1-num2
    elif what_to_do=="multiply":
        return num1*num2
    elif what_to_do=="divide":
        if num2!=0:
            return num1/num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
what_to_do=input("enter the operation you want to perform (add, subtract, multiply, divide): ")
print(calcu(num1,num2,what_to_do))


#_____________________________________________________________

person={"Alice":{"age":18,"city":"New York"},
        "Bob":{"age":25,"city":"Los Angeles"},
        "Charlie":{"age":60,"city":"Chicago"},
        "David":{"age":28,"city":"Houston"},
        "Eve":{"age":18,"city":"Phoenix"},
        "Frank":{"age":40,"city":"Philadelphia"},
        "Grace":{"age":27,"city":"San Antonio"},
        "Heidi":{"age":15,"city":"San Diego"},
        "Ivan":{"age":10,"city":"Dallas"},
        "Judy":{"age":19,"city":"San Jose"}}
def check_age_group(person):
    for i in person:
        if person[i]["age"]>=18 and person[i]["age"]<=40:
            print(f"{i} is {person[i]['age']} years old and {i} is adult")
        elif person[i]["age"]<18:
            print(f"{i} is {person[i]['age']} years old and {i} is minor")
        else:
            print(f"{i} is {person[i]['age']} years old and {i} is senior citizen")
check_age_group(person)


