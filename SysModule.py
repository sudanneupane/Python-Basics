### 10th May 2022
# Sys module 

import sys  # we have to import sys module in order to use the method or attribute defined in it

# sys.argv      argv is a command vector which stores command line inputs 

# int main( int arc, char* args[])  # this is an example for main with command line, it is c program example 

# if we want to give input program in command prompt then we have to write program with that support 

# Below is the example for python command line argument

print("My name is {} and phone number is {}".format(sys.argv[1], sys.argv[2]))

for i in range(2):
    if i == 1:
        sys.exit            # sys.exit works like break in a loop
        # sys.exit(0)         # sys.exit(0) teerminates the complete proram
print("Hello")

print(sys.maxsize)          # this gives us the maximum number allowed in the python version
print(sys.path )            # this prints all the path in the python directory 
print(sys.version )         # details about python version and os architecture 

# stdin, stdout, stderr

for i in sys.stdin:           # sys.stdin takes input form keyboard
# for i in input("Enter a character: "):        # same as above
    if i.rstrip() == 'q':     # rstrip() function is used to remove spaces in input towards right side
        sys.exit(0)
    else:
        sys.stdout.write(i)     # sys.stdout works like print 
        # print(i)              # same as above
