            ### 1st May 2022 (revision)
# Classes and objects
# Learn how to write class in python
# learn how to write member data and mamner function in python
# learn to use self
# learn to create object of class
# learn to access member of the class usinf object 

class Queue:
    front = 0
    list = [] 
    rear = 0
    max = 0

    def __init__(self):        # like constructor, in python, __init__() is used to give value to member data of the class
         self.front = 0             # the meaning of self is that it is member of the class Queue. it is like 'this' in java.
         self.list = [] 
         self.rear = 0
         self.max = 3

    def isEmpty(self):
        if(self.front==-1 and self.rear==-1):
            return True
    
    def isFull(self):
        if(self.rear > max-1):
            return True
        else:
            return False
    
    def insert(self, item):
        if(self.isFull()):
            print("Can not insert. QQueue is full")
        else:
            rear = rear+1
            self.list.append(item)
    
    def delete(self):
        if(self.isEmpty()):
            print("Can not delete. Queue is empty.")
        else:

            print("Deleted item is {}".format(self.list.pop(self.front)))
            front = front-1

    def display(self):
        if(self.isEmpty()):
            print("Can not display. Queue is empty.")
        else:
            print(self.list)

ob = Queue()        # object creation in python. __init__ function gets called here 
ob.insert(10)
ob.display()