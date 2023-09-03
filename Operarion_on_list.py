
#   4th April 2022
### Operarion on list.

name = ["abc", "ssh", "xyz"]        # creates list named "name".
print(name[1])                      # accessing the each elements using indexing.
print("Elements are:.")
for x in range(0,3):
    print(name[x])
print("Elements are:.")
for i in name:                      # displaying all elements of the list using for-each loop one by one.
    print(i)
print("Elements are:.")
print(name)                         # displaying all the elements same as it in the list all at once.

print(len(name))                    # to displaythe number of elements in the list using len().

name.append("added")                # this is the way to add new elements to the exisisting list.
print("Elements are:.")
print(name) 

name.pop(2)                         # pop function deletes the element in the list at the given position.
print("Elements are:.")
print(name) 

name.remove("abc")                  # remove function deletes the element in th list, given the value in the argument.
print("Elements are:.")
print(name) 




# 5th April 2022

a = [11, 12, 13, 14, 15, 16, 17, 18, 19]
# List indexing
print( a[0])    # 11       Displays the value in the 0th position 
print( a[3])    # 14

# List negative indexing
print( a[-1])   # 19        Displays values in the last position
print( a[-2])   # 18

# List slicing
print( a[2:6])  # [13, 14, 15, 16]      Displays values starting from position 2 to 6
print( a[2:])   # [13, 14, 15, 16, 17m 18, 19]
print( a[:])    # [11, 12, 13, 14, 15, 16, 17, 18, 19]      Displays all element

print( a[ : : 2])       # Displayed all odd numbers
print( a[ 1: : 2])      # # Displayed all even numbers




print("\nEnd of program. \n")