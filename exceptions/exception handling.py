


try:
    num1 = 7
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print('an error occured due to error dividing by zero')

print('-------------------')

try:
    print('a'+ 5)
    print(7/0)
    
except TypeError:
    print('illegal addition')
except ZeroDivisionError:
    print('illegal division')

print('-------------------')

try:
    variable = 10
    print(10/2)
except:
    print('error')
print('finished')

print('-------------------')

try:
    variable = 10
    print(variable / 0)
    print(variable + 'hello')
    
except ZeroDivisionError:
    print('didied by zero ')   
except (ValueError, TypeError):
    print('error occured') 


print('-------------------')

try:
    word = 'spam'
    print(word / 0)
except:
    print('error')