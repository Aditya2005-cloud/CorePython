# len() works on strings, lists and tuples but not on integers

number = 12345
# num = number % 10   12345 % 10 = 5 it helps to get the last digit of the number
rev = 0
while number > 0:
    digit = number % 10      # get last digit
    rev = rev * 10 + digit
    number = number // 10       # remove last digit
print("Reversed:", rev)
number1=12345
print(str(number1)[::-1]) # another way to reverse a number by converting it to string and slicing it

num=175673
for i in str(num):
    if i == '3':
        print("Digit 3 is present in the number")
        break
  
num1=123
c=0
for i in range(len(str(num1))):
    a=num1%10
    num1=num1//10
    c=c+a
    print(c)
# better veersion of the above code
num2=123
c1=0
while num2 > 0:
    a=num2%10
    num2=num2//10
    c1=c1+a
print(c1)

num3=123
c2=1
while num3 > 0:
    a=num3%10
    num3=num3//10
    c2=c2*a
print(c2)

num4=1233333
count=0
for i in str(num4):
    if i=="3":
        count+=1
print(f"no 3 is presemt {count}time")
# the pure math approach
num4 = 1233333
digit_to_find = 3
count = 0
while num4 > 0:
    digit = num4 % 10
    if digit == digit_to_find:
        count += 1
    num4 = num4 // 10
print("Count:", count)
