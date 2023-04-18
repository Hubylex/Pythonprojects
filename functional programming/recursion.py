## factorial 
from itertools import accumulate
'''def factorial(x):
    if x == 1:
        return 1

    else:
        return x * factorial(x-1)

print(factorial(5))

print('---------')

def count(x):
    if x == 5:
        print(5)
    else:
        print(x) 
        count(x+1)

print(count(1))

print('---------')


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(132))
print(is_even(74))'''

#0,1,1,2,3,5,8,13,21,34



num = int(input()) 

def fibonacci(n): 
    if n <= 1: 
        yield n 
    else: 
        yield fibonacci(n-1) + fibonacci(n-2) 
    
for i in range(num):
    print(fibonacci(i))