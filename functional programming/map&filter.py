##map - takes a funct and argument(iterable)
##eg.list and performs the func on each element of list

def add_five(x):
    return x +5

nums = [11,22,33,44,55]
result = list(map(add_five,nums))
print(result)

## lambda format
numss = [11,22,33,44,55]

print(list(map(lambda x: x+5,numss)))


## filter - filters an iterale by leaving only 
# elements satifisfying condition stated 


##returning only even numbers
nums = [11,22,33,44,55]
res = list(filter(lambda x:x%2==0,nums))
print(res)

## returning odd numbers
nums = [1,2,3,4,5,6]
print(list(filter(lambda x:x%2 != 0,nums)))

print('--------')
def s(a):
    return a+5

lisst = [1,2,3,4]
h = list(map(s,lisst))
print(h)