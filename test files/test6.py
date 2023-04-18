import re
format = r'[189]([0-9]{7})$' 

phone = input()

if re.match(format,phone):
    print('Valid')
else:
    print('Invalid')