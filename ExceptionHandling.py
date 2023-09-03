

# Example 1
try:
    print(a)            # exception occur since variable 'a' is not defined      a=10 or some-value
except NameError:       # NameError is a statement errorname, which is built-in in python, it occurs when the variable are not defined before the use  
    print("a is not defined")

# Example 2 
# Try with multiple except 
try:
    c = 2/0         # divide by zero occured 
except NameError:       # this is the way to write multiple except block with try block 
    print("variable not defined ")
except:
    print("something went wrong")



# Example 3 
# use of else

'''
l = [10,20,30]
print(l[3])
Output error:
Traceback (most recent call last):
  File "e:\Python\ExceptionHandling.py", line 20, in <module>
    print(l[3])
IndexError: list index out of range
'''

try:
    l=[10,20,30]
    print(l[3])# exception occurs, because we are trying to access element in the position beyond array soze 
except:
    print("Arrar out of bound access ") # this line comes when there is exception 
else:
    print("program exceuted correctly") # this line comes when there is NO exception 
# try block must have one except block, it may have else block later 


# Example 4 
# # use of finally 
try:
    print("greeting")
    #print (a)      # for except to run
except:
    print("Some exception occured. ")
finally:
    print("I run all the time :) ")


# Example 5
# nested try-except

try:
    f = open("newfile.txt", "a")        # if the file opened in read mode and if the file doesnot exists, e1 occurs
    try:
        f.write("I am writing this line to the file. ") # if the file is opensd in read node and we are trying to write, e2 occurs  
    except:
        print("Writing Error")      # executes on e2
    finally:
        f.close()       # it is written in finaly bea=cause file should be closed irrespective of error 
except:
    print("File does not exist")        # executes on e1





# Advantages of writing programs using exception handling block 
# 1. We cangive user-friendly error messages
#    