
                ## 6th ma 2022
# it is one of the builtin library in python , sys, platform, os
# Application Program Interface (API), these are builtin functions which comes from different modules

import os       # this is the way to include the functions in os module to our program

# current working directory 
res = os.getcwd()       # getcwd() function returns the path where we are storing our current working files 
print(f"Path before changing {res}")

'''
print("Path after changing ")
os.chdir('../')         # chdir() function is used to change the current working directory 
print(os.getcwd())

p = os.path.join(os.getcwd(), "newdirSudan")    # the join() function in the os module is used to join two paths or string that makes path
os.mkdir(p)     # mkdir() function creates a directory as per the pathpassed as the arguments.

# os.makedies() this is used when we want to create multiple directories in a loop

p = os.path.join(os.getcwd(),"newdirSudan")tyyyyyuylyu



os.rmdir(p)         # rmdir() function is used to delete directoory or folder.


'''

# print(os.listdir())      # listdir() function is used to display all the files and directories of the current working directory

print(os.name)          # os.name attribute gives the nam of the current working os name 

# os.error, any error that is returned or displayes during reutime or execution OSError, NameError, IOError

# os.open , function is used to do both read and write operation at both ends of the pipe that is created. 
# os.close(), function is used to close the pipe that is created using os.open()
# 
# os.rename(), used to change the file name
#  

print(os.path.exists("newdirSudan"))        # False, because the E:\PYTHON has no file or directory named "newdirSudan"

# os.paths.getsize("filename"), it returns the size of the file