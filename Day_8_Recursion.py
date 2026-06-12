#Recursion A function calls itself.
def countdown(n):
    print(n)
    if n > 0:
        countdown(n-1)#call itself
countdown(int(input("Enter a number: ")))