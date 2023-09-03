### 9th May 2022

# Stack program in python

# implementation of dynamic stack

# from inspect import isfunction


class Stack:
    def __init__(self):
        self.max = 3
        self.count = 0
        self.element = []       # empty list is created

    def isEmpty(self):
        return self.element == []       # checking whether the list is empty 
    
    def ifFull(self):
        return self.max == self.count

    def push(self, val):
        self.element.append(val)        # adding element into the stack
        self.count = self.count+1

    def pop1(self):
        return self.element.pop()       # removing element from the stack
    
    def disp(self):
        print(self.element)

ob1 = Stack()
x = 'y'
while(x=='y'):
    print("\n1. push, 2. pop, 3. display ")
    ch = int(input(" Enter your choice. "))
    if ch == 1:
        if(ob1.ifFull()):
            print("Stack is full.")
        else:
            ob1.push(int(input("Enter a value: ")))
    elif ch == 2:
        if ob1.isEmpty():
            print("Stak is empty. ")
        else:
            print("deleted element is {}".format(ob1.pop1()))
    elif ch == 3:
        if ob1.isEmpty():
            print("Can not display in empty stack.  ")
        else:
            ob1.disp()

    x = input("\nPress 'y' to continue. ")
print("\nEnd of Program.\n\n")




