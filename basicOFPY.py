# #different type of variables
# from curses.ascii import isalpha

a = 10  # int: integer
b = 3.14 # float: floating point number
coordinates = 3 + 5j  # complex: complex number
c = "Hello, World!"  # str: string 
print(c[0])  # Output: 'H' (accessing the first character of the string) []is used to access individual characters in a string by their index. In this case, c[0] retrieves the first character of the string "Hello, World!", which is 'H'. The index starts at 0, so c[1] would give you 'e', c[2] would give you 'l', and so on. its start from 0 to n-1 where n is the length of the string.its can also be used to access a range of characters (called slicing) by specifying a start and end index, like c[0:5] which would give you 'Hello'.[0:5:2] would give you 'Hlo' (every second character from index 0 to 4).its also use -1 to access the last character of the string, so c[-1] would give you '!' (the last character of "Hello, World!"). Similarly, c[-2] would give you 'd', c[-3] would give you 'l', and so on, counting backwards from the end of the string. This allows you to easily access characters from the end without needing to know the exact length of the string.
# \\ is used to include a literal backslash in a string. For example, if you want to represent a file path on Windows, you might write "C:\\Users\\Username\\Documents". The double backslash ensures that the backslash is treated as a literal character rather than an escape character.
# \n is used to represent a newline character in a string. When you include \n in a string, it creates a line break. For example, "Hello\nWorld" would be displayed as:
# \ is used to escape special characters in a string, allowing you to include characters that would otherwise be interpreted differently. For example, if you want to include a double quote inside a string that is enclosed in double quotes, you can use the backslash to escape it: "She said, \"Hello!\"". This way, the inner double quotes are treated as part of the string rather than as delimiters.
len(c) # 13 (length of the string)
# isalpha()
# Checks if all characters in the string are letters (A–Z, a–z) and the string isn’t empty.
# isalnum()
# Checks if the string contains only letters and numbers (no spaces or symbols).
# isdecimal()
# Returns True if all characters are decimal digits (0–9).
# lower()
# Converts all letters in the string to lowercase.
# islower()
# Checks if all cased characters in the string are lowercase.
# upper()
# Converts all letters in the string to uppercase.
# isupper()
# Checks if all cased characters are uppercase.
# title()
# Converts the string so that each word starts with a capital letter.
# startswith()
# Checks if the string begins with a specific substring (you pass it as an argument).

d=True  # bool: boolean (True/False)

#how to convert one data type to another
numbers=float(10) # type conversion: converts integer 10 to float 10.0
print(numbers)  # Output: 10.0

# arethmetic operators
print(10 + 5)   # 15
print(10 - 5)   # 5
print(10 * 5)   # 50
print(10 / 5)   # 2.0
print(10 // 3)  # 3 (floor division) is used to divide two numbers and round down to the nearest whole number. In this case, 10 divided by 3 is approximately 3.33, but floor division rounds it down to 3.
print(10 % 3)   # 1 (modulus) its gives the remainder of the division
print(10 ** 2)  # 100 (exponentiation) is used to raise a number to the power of another number. In this case, 10 is raised to the power of 2, resulting in 100.

#  relational operators
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(5 <= 3)   # False

# logical operators
True or False   # (boolean) is a logical operator that returns True if at least one of the operands is True, and False otherwise. In this case, since the first operand is True, the result will be True.
print(True or False)   # True
print(False or False)  # False
True and False  # (boolean) is a logical operator that returns True only if both operands
print(True and True)    # True
print(True and False)   # False
print(not True)   # False is a logical operator that negates the value of the operand. In this case, since the operand is True, the result will be False.
print(not False)  # True is a logical operator that negates the value of the operand. In this case, since the operand is False, the result will be True.

# --- Sequence Types ---
fruits = ["apple", "pear"]  # list: mutable collection
colors = ("red", "blue")    # tuple: immutable collection
numbers = range(1, 6)       # range: sequence from 1 to 5
a = [1, 2]
b = a.copy() # Creates a new list that is a copy of 'a'
a = [1, 2, 3]
a.reverse()   # [3, 2, 1]  reverses the order of the list in place (modifies the original list)
a = [3, 1, 2]
a.sort()   # [1, 2, 3] sorts the list in place (modifies the original list) in ascending order. You can also use a.sort(reverse=True) to sort in descending order. The sort() method does not return a new list; it returns None because it modifies the original list directly. If you want to get a sorted version of the list without modifying the original, you can use the sorted() function, which returns a new sorted list. For example: sorted_a = sorted(a)  # This will return a new sorted list [1, 2, 3] without changing 'a'. 
a = [1, 2, 2, 3]
a.count(2)   # 2 counts how many times the value 2 appears in the list 'a'. In this case, since 2 appears twice in the list [1, 2, 2, 3], the result will be 2.
a = [10, 20, 30]
a.index(20)   # 1 returns the index of the first occurrence of the value 20 in the list 'a'. In this case, since 20 is located at index 1 (the second position in the list), the result will be 1. If the value is not found in the list, it will raise a ValueError.
a = [1, 2]
a.clear()   # [] clears all items from the list 'a', resulting in an empty list. After calling a.clear(), the list 'a' will be [].
a = [1, 2, 3]
a.pop()     # returns 3 → [1, 2]
a.pop(0)    # returns 1 → [2] removes and returns the item at the specified index. If no index is provided, it removes and returns the last item in the list. In this case, a.pop() removes and returns 3 from the list [1, 2, 3], leaving [1, 2]. Then, a.pop(0) removes and returns 1 from the list [1, 2], leaving [2].
a = [1, 2, 2, 3]
a.remove(2)   # [1, 2, 3] removes the first occurrence of the value 2 from the list 'a'. In this case, since 2 appears twice in the list [1, 2, 2, 3], only the first 2 will be removed, resulting in the list [1, 2, 3]. If the value is not found in the list, it will raise a ValueError.
a = [1, 3]
a.insert(1, 2)   # [1, 2, 3] inserts the value 2 at index 1 in the list 'a'. In this case, since index 1 is the second position in the list, the value 2 will be inserted between 1 and 3, resulting in the list [1, 2, 3]. The insert() method does not replace any existing elements; it shifts them to the right to make room for the new element.
a = [1, 2]
a.extend([3, 4])   # [1, 2, 3, 4] extends the list 'a' by appending all the items from the iterable (in this case, another list [3, 4]) to the end of 'a'. After calling a.extend([3, 4]), the list 'a' will be [1, 2, 3, 4]. The extend() method modifies the original list in place and does not return a new list.
a = [1, 2]
a.append(3)   # [1, 2, 3] appends the value 3 to the end of the list 'a'. After calling a.append(3), the list 'a' will be [1, 2, 3]. The append() method modifies the original list in place and does not return a new list.
a = [3, 1, 2]
b = sorted(a)
print(b)  # [1, 2, 3]
print(a)  # [3, 1, 2] (unchanged) The sorted() function returns a new sorted list from the items in the iterable (in this case, the list 'a') without modifying the original list. In this example, 'b' will be a new list containing the sorted elements [1, 2, 3], while 'a' remains unchanged as [3, 1, 2].

# converting
Name=[]# empty list
permanent_Names=tuple(Name)# converting list to tuple
name = list(permanent_Names) # converting tuple to list
set_of_names = set(name) # converting list to set (removes duplicates)

frozen_ids = frozenset([1, 2, 3]) #Like set, but cannot be changed

# --- Mapping & Set Types ---
user = {"id": 1, "bio": "Hi"} # dict: key-value pairs
unique_ids = {101, 102, 103}  # set: unique items only

# nested Dictionary
students = {
    "s1": {"name": "A", "marks": 80},
    "s2": {"name": "R", "marks": 70}
}

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
 #  called, but result is ignored havent been printed or stored in a variable
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


try:
    # code that may cause error
    pass# pass means "do nothing". It's a placeholder that allows you to write code that syntactically requires a statement but you don't want to execute anything.
except:
    pass
    # runs if error happens
finally:
    pass
    # always runs (error or not)