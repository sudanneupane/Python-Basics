#   6th April 2022

# Functions set of programming instructions written to perform some specific task
#            

def funName():              # function defination without argument and without return 
    print("Hello World ")


def additions(x,y):          # function defination with arguments without return
    print(x+y)

def subtraction(x,y):
    print(x-y)

def multiplication(x,y):
    print(x*y)

def division(a,b):          # function defination with arguments with return
    return a/b

def remainder(a,b=2):          # function defination with arguments with return with default value
    return a%b                 # defiault value is used only when the argument is not passed in the function call

i = 50
j = 10
funName()           # function call that executes function defination 
additions(i,j)
subtraction(i,j)
multiplication(i,j)
print(division(i,j))
print(remainder(12,5))
print(remainder(12))