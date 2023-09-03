'''
March 12 2022

String

'''


str= "collection of characters"
print(str[4])
for i in str:       #for-each loop in python
    print(i)

print(str)
print(str.__len__())       #finding length of given string
print("xyz".__len__())
print(len(str))  
a="xyz"
print(a*3)      # repeat the stirng
print("of" in str )     # boolean result
print(str.find("of"))   #gives the postition of the string at first occurance
print(str.replace("of","to"))   #replaces 'of' to 'to   . changes made inside print applys only to that line
print(str)
str = str.replace("of","to")    
print(str)