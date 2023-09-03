    ##     11th April 2022
    # touuple follows ordered, allows duplicates, not mutable

from filecmp import cmp


# a = (1, 2, 3, 3)
# print(a)
# print(len(a))

# b = (10, )      # singleton
# x = (10)
# print(f"{b} comma vs no comma {x}")

# c = ( )                    # empty tuple
# print(c)

# d = (1, True, "abc", 2.3, 'x')
# print(d)

# print(type(a))              # type() function is used to know the type of the value used

# # Ither war=y to create tuple
# a = tuple((10, 20, 30))     #using builtin tuple() function
# b = (1, 2, 3)
# c = a+b
# print(c)

# a1 = (10, 20, 30)
# b1 = (11, 22, 33)
# c1 = a1+b1
# print(c1)

# print(a*3)                  # displays tuple elements three times
# print(a[::-1])              # displays the elements in reverse order

# #del a[0]                    # it gives error because tuple doesnot allows changes.
# print(a)

# b3 = [111, 222, 333, 444]
# print(type(b3))
# print(b3)
# c3 = tuple(b3)
# print(type(c3))
# print(c3)

# for i in c3:
#     print(i)

a3 = tuple((10, 20, 30))  
a4 = tuple((11, 22, 31))  
print(min(a3))
print(max(a4))
print(cmp(a3,a4))

'''
Got error

# if(cmp(a3,a4) != 0):
#     print("not same")
# else:
#     print("same")
'''
