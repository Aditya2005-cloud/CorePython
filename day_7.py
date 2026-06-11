#**kwargs
# *args example
def fun(*args):
    return sum(args)
print(fun(5, 10, 15))

# **kwargs example
def fun(**kwargs):
    for key, val in kwargs.items():
        print(key, val)
fun(a=1, b=2, c=3)

# **kwargs collects many named arguments
def student(**details):
    print(details)
student(name="Bob", age=30, grade="A")