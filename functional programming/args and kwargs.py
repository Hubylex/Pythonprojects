def func(named_arg,*args):
    print(named_arg)
    print(list(args))

func(1,2,3,4,5)

print('---------')

a, b , c, *d = 1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)
print(d)


print('---------')

def f(a,*b):
    print(a)
    print(b)
print(f(1,2,3))

print('---------')

def f(x, y=9 ,*s ,**t):

    print(x)
    print(y)
    print(s)
    print(t)

f(2,3,4,5,6 , a=7 , b=8, c = 9)