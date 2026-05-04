# Print numbers 1 to 20
for n in range(1,21):
    print(n)

# Print even numbers from 1 to 50
for n in range(1,51):
    if n%2==0:
        print(n)

# Sum of numbers from 1 to 100
sum_number=0
for i in range(1,101):
    sum_number+=i
print(f"the sum of number from 1 to 100 is {sum_number}")

# Count how many even numbers are in 1 to 50
total=[]
for i in range(1,51):
    if i%2==0:
        total.append(i)
print(f"the length of total is {len(total)}")

# Sum of odd numbers from 1 to 50
sum_odd=0
for i in range(1,51):
    if i%2!=0:
        sum_odd+=i
print(f"the sum of odd number from 1 to 50 is {sum_odd}")

# Largest of 3 numbers
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
else:    
    print(f"{num3} is the largest number")

# Reverse a number
# % gives last digit
# // removes last digit
# num=int(input("enter a number: "))
# reverse=0
# while num>0:
#     last_digit=num%10
#     reverse=reverse*10+last_digit
#     num=num//10
# print(f"the reversed number is {reverse}")
# but this method does not work for negative numbers and numbers ending with 0
num=int(input("enter a number: "))
reverse=int(str(num)[::-1])

#MINI PROJECT(Student Pass/Fail System)
student={"s1":{"name":"Alice","marks":85},
        "s2":{"name":"Bob","marks":72},
        "s3":{"name":"Charlie","marks":20}}
for s in student:
    if student[s]["marks"]<=30:
        print(f"{student[s]['name']} has failed in the exam with marks {student[s]['marks']}")
    elif student[s]["marks"]>30 and student[s]["marks"]<=60:
        print(f"{student[s]['name']} has passed in the exam with marks {student[s]['marks']}")
    else:
        print(f"{student[s]['name']} has passed in the exam with marks {student[s]['marks']} and got distinction")
#   ______________or_______________
for s in student.values():
    if s["marks"]<=30:
        print(f"{s['name']} has failed in the exam with marks {s['marks']}")
    elif s["marks"]>30 and s["marks"]<=60:
        print(f"{s['name']} has passed in the exam with marks {s['marks']}")
    else:
        print(f"{s['name']} has passed in the exam with marks {s['marks']} and got distinction")