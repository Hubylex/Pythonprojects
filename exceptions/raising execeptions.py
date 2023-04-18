'''num = int(input())
if num > 100:
    raise ValueError('invalid input')

try:
    name = input()
    if len(name ) < 4:
        raise ValueError(' name is invalid')
except:
    print('invalid name')
else:
    print('account created')


try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError'''

try:
    print(1)
    print(20/0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)

x = 3
try:
    x += '2'
except:
    x += 2
else:
    x += 4 
finally:
    print(x)