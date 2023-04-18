import re
password ='f6f36W'

format = r'.*[A-Z]'
format_2 = r'.*[0-9]'

if re.search(format,password) and re.search(format_2,password):
    print('match')
else:
    print('no match')


#- it has at least one uppercase character
#- it has at least one number