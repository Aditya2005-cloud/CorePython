import sys

# Print interpreter details
print(f"Python Version: {sys.version}")
print(f"Operating System: {sys.platform}")

# Check command line inputs
print(f"Script Name: {sys.argv[0]}")

# Check memory size of an integer
#How much memory (RAM) is this object using
print(f"Memory size of 42: {sys.getsizeof(42)} bytes")

# Gracefully stop the program
sys.exit(0)