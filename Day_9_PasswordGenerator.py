import random

ch="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def gen_pass(c):    
    password=""
    for i in range(c):
        password+=random.choice(ch)
    print(password)
c=int(input("Enter the number of characters for the length of password: "))
gen_pass(c)