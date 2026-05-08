nums = [10, 20, 30, 40]
#Access elements
print(nums[0])
print(nums[-1])
#Loop through list
for i in nums:
    print(i)
#List slicing
print(nums[1:3])
print(nums[::-1])
#Find sum of all list elements
sum=0
for i in nums:
    sum+=i
print(sum)
#Find largest number in list
max_num=0
for i in nums:
    if i>max_num:
        max_num=i
print(max_num)
# Count even numbers in list
counting1=0
for i in nums:
    if i%2==0:
        counting1+=1
print(f"the number of even numbers are {counting1}")
#
user_list=int(input("enter the number of elements you want in the list: "))
num_list=[]
for i in range(user_list):
    num=int(input("enter the number u want to insert: "))
    num_list.append(num)
print(num_list)
# Pattern printing
for i in range(0,5):
    for a in range(0,i):
        print("*",end=" ")
    print()
print("----------------------------------")
for i in range(5,0,-1):
    for a in range(0,i):
        print("*",end=" ")
    print()
#Student Marks Analyzer
# Program should:
# Find highest marks
# Find average
# Count passed students (≥ 40)
marks = [78, 45, 90, 34, 88]
highest_marks=0
average=0
count=0
for i in marks:
    if i>highest_marks:
        highest_marks=i
    average+=i
    if i>=40:
        count+=1
average=average/len(marks)
print(f"the highest marks are {highest_marks}")
print(f"the average marks are {average}")
print(f"the number of passed students are {count}")
#Find smallest number in list
min_num=marks[0]
for i in marks:
    if i<min_num:
        min_num=i
print(f"the smallest number in the list is {min_num}")
#Remove duplicates from list
marks1=list(set(marks))#remove duplicates
print(marks1)
#Count odd numbers
count1=0
for i in marks:
    if i%2!=0:
        count1+=1
print(f"the number of odd numbers are {count1}")
#Reverse list WITHOUT [::-1]
for i in range(len(marks)-1,-1,-1):
    print(marks[i])