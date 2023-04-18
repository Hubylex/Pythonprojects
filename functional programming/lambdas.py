##lambda function
'''print((lambda x : x ** 2 + 5*x + 4)(-4))

a = (lambda x : x*x)(8)
print('a',a)

s = (lambda x: x+1)(3)
print('s',s)

greet_me = lambda: 'hello'

strip_upper = lambda s: s.strip().upper()
strip_upper(" hello ")'''


##recursive func for fctorial

'''def rec(n):
    if n == 1:
        return 1
    else:
        return n*rec(n-1)
print(rec(int(input())))'''

#fibonacci series

# 0,1,1,2,3,5,8,13,21,34

def fib(n):
    i = 0
    while i<=n:
        result = i+ fib(i+1)
        yield result
        i+=1
for result in fib:
    print(result)

print(fib(3))