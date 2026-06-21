try:
    print(10/0)
except ZeroDivisionError:
    print("You cannot divide by zero")

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a number")

# Very Important (learn these first)
#   ZeroDivisionError for division by zero
#   ValueError for invalid input
#   TypeError for type mismatch
#   NameError fro variable not defined
#   IndexError for index out of range
#   KeyError for key not found
#   AttributeError fro attribute not found
# Important
#   ImportError for module not found
#   ModuleNotFoundError for module not found
#   FileNotFoundError for file not found
#   PermissionError for permission denied
#   RuntimeError for unexpected runtime error
#   RecursionError for too much recursion
# Useful to know
#   StopIteration for iterator exhausted
#   EOFError for end of file
#   AssertionError for assertion failed
#   NotImplementedError for method not implemented
#   UnicodeError for Unicode related error
#   OverflowError for integer overflow
# Networking/System related (later)
#   OSError for operating system error
#   TimeoutError for operation timeout
#   ConnectionError for network connection error
#   BrokenPipeError for broken pipe
#   ConnectionResetError for connection reset