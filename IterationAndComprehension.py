## 1st May 2022 (Revision class)

# Iterator and Comprehensions

list1 = [1,2,3,4,5,6]
temp = []
for i in list1:
    if (i%2==0):
        temp.append(i)
    print(temp)

# Below line tries to compress the above four line to only 1 line
temp1 = [ i for i in list1 if i%2==0]
print(temp1)

itr = iter(list1)       # iter() function returns an object refrence to the array that is passed as aegumenrt 
print(itr)
print(next(itr))        # next() function automatically displays the next value in the array because it takes the iterator-object as argument 
print(next(itr))
print(next(itr))
print(next(itr))
