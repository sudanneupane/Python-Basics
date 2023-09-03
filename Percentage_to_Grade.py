'''24 Feb 2022 
Program to check Grade taking percentage as input using else if condition

'''

p=85
if(p<=100 and p>90):            
    print("You got A+ grade")
elif(p<=90 and p>80):
    print("You got A grade")
elif(p<=80 and p>70):
    print("You got B+ grade")
elif(p<=70 and p>60):
    print("You got B grade")
elif(p<=60 and p>50):
    print("You got C+ grade")
elif(p<=50 and p>50):
    print("You got C grade")
elif(p<=50 and p>40):
    print("You got D+ grade")
elif(p<=40 and p>30):
    print("You got D grade")
else:
    print("You got F grade")



'''24 Feb 2022 
Program to check Grade by taking percentage as input using nestedif condition

'''
p=43
grade=''
if p>40:
    grade ='D'
    if p>50:
        grade ='C'
        if p>70:
            grade ='B'
            if p>80:
                grade ='A'
else:
    grade='F'
print(f"Grade {grade}")  # Same as print("Grade",grade)
