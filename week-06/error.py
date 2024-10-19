import os
import sys

# TODO: Check first that the arguments you were expecting are present
try:
    names = os.listdir(sys.argv[1])
    for name in names:
        print(name)
except Exception as error:
    print("EROR",type(error))

