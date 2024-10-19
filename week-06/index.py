import os 
import sys

# TODO: Check first that the arguments you were expecting are present

if(len(sys.argv)!=1):
    path = sys.argv[1]
    file_exists = os.path.exists(path)
    if(file_exists):
        names = os.listdir(path) 
        for name in names: 	print(name)
else:
    print("you need to pass an argument")


try:
    print(5/0)
except ZeroDivisionError:
    print(" you cannot devide by zero")