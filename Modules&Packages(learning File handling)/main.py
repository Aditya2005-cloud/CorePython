import calculater
# #Bring the entire calculator.py file.because we imported the whole file.
# Python loads the entire file into memory.Read the file and make its contents available.
# But it does NOT run every function.
# Functions are only defined and kept ready.
# Nothing happens until you call them.

print(calculater.add_num(10, 20))

#Import only one 
from calculater import add_num#Import only one function
print(add_num(10, 20))
#or 
# print(calculater.add_num(10, 20))

# but other will not work like print(sub_num(10, 20)) 

from time import Time
# from  -> from this file
# time   -> time.py
# import -> bring
# Time   -> the Time class

#and what if the file i want is not presend in current folder or in current drive how to bring it up
#we can import the file from another folder or drive
from PracticeFolder_Python.calling_thisFile import WecanCall
#PeacticeFolder_Python is the folder name and calling_thisFile is the file name
#and we r importing the WecanCall class from calling_thisFile file


#from this u can import any class from any file or any drivers in your pc or any folder like pendrive
import sys
sys.path.append(r"U have to past your path here")
from file_name import Class_name

#Small correction: Python doesn't care about drives (C:, D:).
# It cares about folders in its search path. 
# If a folder isn't in the search path, Python can't import from it until you add it.