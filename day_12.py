a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
try:
    def add_num(a,b):
        if a>=0 and b>=0:
            return a+b
        else:
            print("Invalid input")
except:
    print("Invalid input as u have use negative numbers")
finally:
    print("You have completed the task")

print(add_num(a,b))