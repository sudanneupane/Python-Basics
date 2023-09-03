### monotonic or not (ascending/decending  or not)
#   4th April 2022

num0 = [1,2,3,4,5]

print( all( num0[i] <= num0[i+1] for i in range(len(num0)-1)) or all( num0[i] >= num0[i+1] for i in range(len(num0)-1)) )

num1 = [5,4,3,2,1]

print( all( num1[i] <= num1[i+1] for i in range(len(num1)-1)) or all( num1[i] >= num1[i+1] for i in range(len(num1)-1)) )


num2 = [1,2,3,5,4]
print( all( num2[i] <= num2[i+1] for i in range(len(num2)-1)) or all( num2[i] >= num2[i+1] for i in range(len(num2)-1)) )


def check_monotonic(num):
    result = all( num[i] <= num[i+1] for i in range(len(num)-1)) or all( num[i] >= num[i+1] for i in range(len(num)-1))
    return result

num3 = [5,4,6,2]
print(check_monotonic(num3))