#Sum of a list
nums = [10, 20, 30, 40]
sum=0
for i in range(len(nums)):
    sum=sum+nums[i]
print(sum)

#Count vowels
name = "education"
count=0
for i in range(len(name)):
    if name[i] in "aeiou":
        count+=1
print(count)

#Pass/Fail Function
def check_result(marks):
    if marks>=30:
        return "Pass"
    else:
        return "Fail"

marks=int(input("Enter the marks: "))
print(check_result(marks))

#Reverse a number
a=1234
print(str(a)[::-1])
#or
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)

#dict
students = {
    "Aditya": 85,
    "Rahul": 30,
    "Aman": 72
}
for i in students:
    print(f"{i} got {students[i]} marks")
#we can also use to call key value directly
for key, value in students.items():
    print(f"{key} {value}")

#Count failed students
for key in students:
    if students[key]<40:
        print(students[key])

#Find topper
for key in students:
    if students[key]==max(students.values()):
        print(f"{key} is the topper {students[key]}")

#Mini Project
students = {
    "Aditya": 85,
    "Rahul": 30,
    "Aman": 72,
    "Priya": 95
}
# Print Pass/Fail for each student
for i in students:
    if students[i]>=40:
        print(f"{i} passed")
    else:
        print(f"{i} failed")
# Count passed students
count=0
for i in students:
    if students[i]>=40:
        count+=1
print(count)
# Count failed students
count=0
for i in students:
    if students[i]<40:
        count+=1
print(count)
# Find topper
for key in students:
    if students[key]==max(students.values()):
        print(f"{key} is the topper {students[key]}")

#Student Average
students = {
    "Aditya": [80, 90, 70],
    "Rahul": [50, 60, 40],
    "Priya": [95, 85, 90]
}
for i in students:
    sum=0
    for j in range(len(students[i])):
        sum=sum+students[i][j]
    print(f"{i} average is {sum/len(students[i])}")
#Find Overall Topper
for key in students:
    if sum(students[key])/len(students[key])==max(students.values()):
        print(f"{key} is the topper {sum(students[key])/len(students[key])}")
#Count Students Above Average 75
count=0
for key in students:
    if sum(students[key])/len(students[key])>=75:
        count+=1
print(count)