'''Common exceptions
    
Import error: wen n import fails
index error : a list is indexed with an out-of-rnge number
name error : an unknown vriable is used 
syntax error : the code cnt be parsed properly
type error : a function is called on a value of an inappopriate type
value error : a functio is called on a value of the correct type but with with an inappopriate value

type error
>'a' + 8     -- the function + is called on a number and an str(which is an inappopriate type)

value error 
int('a')     -- the funtion int is called on a string(appopriate type) 
                but the vlue in the string is 'a' which is inappopriate(int works with numbers)

>import math
>math.sqrt(-1)


'''
