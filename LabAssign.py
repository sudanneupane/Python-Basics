#####       Sudan Neupane
#####       20BTRIS055
#####       ISE
#####       4th semester
#####       Python Lab
'''
# 1. Python Program to check Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10    
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# 2. Python Program to find position of n\'th multiple of a number k in Fibonacci Series
def findPosition(k, n):
    f1 = 0
    f2 = 1
    i =2
    while i!=0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        if f2%k == 0:
            return n*i
        i+=1
    return
n = 5       # Multiple no.
k = 4       # Number of whose multiple we are finding
print("Position of n\'th multiple of k in"
                "Fibonacci Series is", findPosition(k,n))
 
readFile = open("first.txt", "r") 
writeFile = open("updated.txt", "w") 


# 3. Python Program to check if given array is Monotonic

def isMonotonic(A):
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A = [1,2,3,4,7,8]
print(isMonotonic(A))


# 4. Sort the values of first list using second list

def sorting(list1, list2):
    res = zip(list2,list1)
    finalresult = [ i for _ , i in sorted(res)]
    return finalresult

list1 = ["mss", "jannutal", "vatsal", "kamya", "sudan", "salahuddin", "smaraj"]
list2 = [1,2,0,0,2,1,1]
print(sorting(list1, list2))



# 11. Python program to implement stack with all its cases

class Stack:
    def __init__(self):
        self.element = []       # empty list is created

    def isEmpty(self):
        return self.element == []       # checking whether the list is empty 

    def push(self, val):
        self.element.append(val)        # adding element into the stack

    def pop1(self):
        return self.element.pop()       # removing element from the stack

    def peek(self):
        return self.element[-1]
    
    def disp(self):
        print(self.element)

s = Stack()
print(s.isEmpty())
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.isEmpty())
s.peek()
s.pop1()
s.disp()
s.pop1()
s.pop1()
s.pop1()
s.peek()
s.pop1()
print(s.isEmpty())
'''
# 12. Python program to copy odd lines of one file to other
readFile = open("first.txt", "r") 
writeFile = open("updated.txt", "w") 

lines = readFile.readlines() 
print(lines)
# type(lines) 
# for idx in range(0, len(lines)): 
# #check for odd lines
#     if(idx % 2 != 0): 
#         writeFile.write(lines[idx]) 
#     else: 
#         pass
# writeFile.close() 
# readFile.close() 
# writeFile = open("updated.txt", "r") 


# lines1 = writeFile.read() 


# print(lines1) 
# writeFile.close()
