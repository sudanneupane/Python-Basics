###     25th April 2022
# sort the first using second list
'''
list1 = ["mss", "jannutal", "vatsal", "kamya", "sudan", "salahuddin", "smaraj"]
list2 = [1,2,0,0,2,1,1]

# Output expected = ["vatsal", "kamya", "mss", "salahuddin", "smaraj", "jannutal", "sudan", ]

res = zip(list2,list1)  #zip() function maps the elements in two list to come as a dictionary elemnt as below line 

print(res)

# after zip, the res internally represented as, { 1:"mss", 2:"jannutal", 0:"vatsal", ...... ,1:"smaraj" }

finalresult = [ i for _ , i in sorted(res)]  # sorting the zipped result and displaying. 'for _ ' meaning, repeat any number of times until the desired output is achieved 

print(finalresult)
'''

def sorting(list1, list2):
    res = zip(list2,list1)
    finalresult = [ i for _ , i in sorted(res)]
    return finalresult

list1 = ["mss", "jannutal", "vatsal", "kamya", "sudan", "salahuddin", "smaraj"]
list2 = [1,2,0,0,2,1,1]
print(sorting(list1, list2))

list3 = [ "My", "name", "is", "happy"]          # list2's value is assigned to list1 and list2 is arranged in ascending order
list4 = [ 3, 4, 2, 1]
print(sorting(list3, list4))