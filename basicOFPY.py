#different type of variables
a = 10  # int: integer
b = 3.14 # float: floating point number
coordinates = 3 + 5j  # complex: complex number
c = "Hello, World!"  # str: string
d=True  # bool: boolean (True/False)

# --- Sequence Types ---
fruits = ["apple", "pear"]  # list: mutable collection
colors = ("red", "blue")    # tuple: immutable collection
numbers = range(1, 6)       # range: sequence from 1 to 5

frozen_ids = frozenset([1, 2, 3]) #Like set, but cannot be changed

# --- Mapping & Set Types ---
user = {"id": 1, "bio": "Hi"} # dict: key-value pairs
unique_ids = {101, 102, 103}  # set: unique items only

# --- None Type ---
result = None    # NoneType: represents "no value"

# bytes: Immutable (cannot change)
# The 'b' prefix tells Python this is bytes, not a string
data = b"hello"
view = memoryview(data)

# bytearray: Mutable (can be changed)
editable_data = bytearray(b"Hello")
editable_data[0] = 74  # Changes 'H' to 'J' (74 is the ASCII code for J)
# print(editable_data) -> bytearray(b'Jello')

from collections import namedtuple, deque

# namedtuple: A tuple where items have names
# Great for making your code easier to read
Point = namedtuple('Point', ['x', 'y'])
pt = Point(10, 20)
print(pt.x)  # Output: 10 (much cleaner than pt[0])

# deque: A list optimized for "popping" from the left side
# Standard lists are slow at removing the first item; deques are fast.
queue = deque(["Alice", "Bob", "Charlie"])
queue.popleft() # Removes "Alice" instantly

# A generator function
def countdown(n):
    while n > 0:
        yield n  # This 'yields' the value instead of returning a whole list
        n -= 1

timer = countdown(5)
print(next(timer)) # Output: 5
print(next(timer)) # Output: 4


print(type(a)) # <class 'int'>
print(isinstance(a, int))  # True,
#isinstance() checks whether a variable belongs to a certain data type

# basic of function
def greeting():
    return"hi...!"

store=greeting()
#OR
greeting() # This will call the function but not store the result anywhere
 # ⚠️ called, but result is ignored havent been printed or stored in a variable
print(store)

# function with parameters
def add_numbers(x, y):
    return x + y
result = add_numbers(5, 3)
print(result)  # Output: 8
#or
print(add_numbers(5, 3))  # Output: 8

# function with default parameters
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

# function with variable-length arguments
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

# function with keyword arguments
def describe_person(name, age):
    return f"{name} is {age} years old."
print(describe_person(name="Bob", age=30))  # Output: Bob is 30 years old.

# function with both *args and **kwargs
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
display_info(1, 2, 3, name="Charlie", age=25)

# function with a docstring (used for documentation)
def multiply(x, y):
    """Returns the product of x and y."""
    return x * y
print(multiply(4, 5))  # Output: 20
print(multiply.__doc__)  # Output: Returns the product of x and y.

# function with a lambda (anonymous function)
square = lambda x: x * x
print(square(6))  # Output: 36

# function with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# function with a generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_sequence = fibonacci(10)
print(list(fib_sequence))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# function with a decorator
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
@uppercase_decorator
def say_hello():
    return "hello"
print(say_hello())  # Output: HELLO

# function with a closure
def outer_function(msg):
    def inner_function():
        return f"Message: {msg}"
    return inner_function
my_message = outer_function("This is a closure")
print(my_message())  # Output: Message: This is a closure

# function with a class method
class MyClass:
    @classmethod
    def class_method(cls):
        return "This is a class method."
print(MyClass.class_method())  # Output: This is a class method.

# function with a static method
class Utility:
    @staticmethod
    def static_method():
        return "This is a static method."
print(Utility.static_method())  # Output: This is a static method.

# function with a property
class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
person = Person("Alice")
print(person.name)  # Output: Alice

# function with a lambda and filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# function with a lambda and map
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# function with a lambda and reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
