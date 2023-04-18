import re

pattern = r"huby"

if re.match(pattern,'lexhubylex'):
    print('match')
else:
    print('no match')
if re.search(pattern,'lexhubylex'):
        print('match')
else:
    print('no match')

print(re.findall(pattern,'lexhubylexhubyhuby'))

print('----------')

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


print('----------')
import re

phone_num = '0012330040'

new = r"^00"

new_format = re.sub(new,'+',phone_num)

print(new_format)
