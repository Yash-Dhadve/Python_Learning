#  Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.

import os

dir = os.getcwd()
print("Current working directory is " + dir)

contents = os.listdir(dir)
print("Contents of the directory:")
for item in contents:
    print(item)