'''
class FirstClass:       #defining class
    # a=10                #member data/assigning member variable
    # b=20

    #__init__() function which takes zero number argument
    def __it__(self):       # __init__() is a function like comstructor udsed to assign the values to the member data of the class
        self.a= 0
        self.b= 0
    #__init__() function which takes two argument
    def __init__(self, x, y):
        self.a=x
        self.b=y




# ob1 = FirstClass()      #creating object of class
# #print(a)    #error because  is not defined         
# print(ob1.a, ob1.b)      # accessing member data of the class using operator

ob2 = FirstClass(10, 20)
print(ob2.a, ob2.b)
'''

class Emp:
    def __init__(self):         # __init__() function is called automatically when the object is created
        self.eid = int(input("Enter emp id: "))
        self.ename = input("Enetr Enp namee: ")
        self.edesig = input("Enetr Enp designation: ")

    def disp(self):
        print("EID = {} Ename = {} Edesig = {} ". format(self.eid, self.ename, self.edesig))
        print(f"EID = {self.eid} Ename = {self.ename} Edesig = {self.edesig} ")

e1 = Emp()
e1.disp()

# Assignment:
# write a class named student with the member data id usn name percentage
# use __init__() method to give input with argument
# write a member metho dname findGrade() a, b, c, d , or f 
# write a member methodname disp() to display three student details
# call the class method using object   