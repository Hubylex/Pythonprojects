
# second smallest 

list1 = [5,7,33,55,7,6,3,3,7,6]

## change list1 into set(-does not contain dupicate numbers)

list2 = list(set(list1))

list2.sort()
print('list2',list2)
print(list2[1])