import re

password = 'Huby32lex.37hd'

print('enter password:',password)



format  = r'.{7,15}$'
format_2 = r'^[A-Z]'
format_3 = r'.+[0-9]'

if re.match(format,password) and re.match(format_2,password) and re.match(format_3,password):
    print('Password is valid')
elif not re.match(format,password):
    print('password should have atleast 7 characters and not exceed 15')
    print('your password has',len(password),'characters')
elif not re.match(format_2,password):
    print('start with caps')
elif not re.match(format_3,password):
    print('include numbers')



#atleast 7 characters, start with cap,contain numbers ,small letters