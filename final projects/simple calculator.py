def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def modulo(num1,num2):
    return num1 % num2


num1 = int(input('ENTER FIRST NUMBER: '))
operation = input('doing wat?')
num2 = int(input('ENTER THE SECOND NUMBER: '))

if operation == '+':
      result = addition(num1,num2)
elif operation == '-':
    result = subtraction(num1,num2)
elif operation == '*':
    result = multiplication(num1,num2)
elif operation == '/':
    result = division(num1,num2)
elif operation == '%':
    result = modulo(num1,num2)

print(num1,operation,num2,'=',result)