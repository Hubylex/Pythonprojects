try:
    print('hello')
    print(1/0)
except ZeroDivisionError:
    print('didded by zero')
finally:
    print('the code cant run')


"""
illustration of try, except, finally
"""
def mytry (divisor):
    try:
        print("1. Hello")
        print("2.", 1 / divisor)
    except ZeroDivisionError:
        print("3. Divided by zero")
        
    finally:
        print("4. This code will run no matter what")
    print("5. This code sometimes won't run")

mytry(1)   # no error
print(10*"-")
mytry(0)   # expected error
print(10*"-")
#mytry("a") # unexpected error           

'''te code above illustrates that the finally block occures no matter wat even if theres an error whereas the next line normaly 
gets executed but fails to do so when an error occurs
this is useful to run important  commands even if theres an error'''


try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

print('-------------------')
try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
'''the else block runs wen no error occurs in the try statement'''