#basic calculator using functions

def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"
    
num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
select=input("Select operation (add, subtract, multiply, divide): ")
if select=="add":
    print(add(num1,num2))
elif select=="subtract":
    print(subtract(num1,num2))
elif select=="multiply":
    print(multiply(num1,num2))  
else:
    print(divide(num1,num2))
