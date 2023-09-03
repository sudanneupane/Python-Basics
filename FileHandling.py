                ## 25th April 2022


# File Handling: 
# functions in file handling program cal=n be: open read(), write(), readline(), readlines(), close() 
# modes of filee can be: 'r'- read, 'w'-write , 'a'-append , 'x'- exexute 
# modes can be written with the type of the file like: t-text or b-binary 


# f1 = open("username.txt", "r")      # opens the existing file named "username.txt" and it is opened for read mode
# #print(f1.read())            # reads the contents in the file 
# # print(f1.read(4))          # reads 13 characters in the file 
# print(f1.readline())         # reads 1 line per function call
# print(f1.readlines())        # displays full content like read(), but line by line 

# f1.close()

# f2 = open("C:\\Users\\NITRO 5\\Desktop\\DAA.txt", "r")  #opens the existing file named DAA and it reads 
# # print(f2.read())

# for i in f2:
#     print(i)    # this also reads line-by-line full file contents

# f2.close()


p1 = open("newfile.txt", "w")       # writes fresh content, if the file does not exist , it creates and then writes
p1.write("Second time I am writing in a file. \n")
p1.close()

p1 = open("newfile.txt", "a")       # continues writing where it stopped previously
p1.write("This will be in the next line in the file. ")
p1.close()

p1 = open ("newfile.txt","r")       # reads if the file is existing, if the file does not exist, it will give error.
print(p1.read())
p1.close()