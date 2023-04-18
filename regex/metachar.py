import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

a = r'....'
if re.match(a,'hello'):
    print('match')
if re.match(a,'baby'):
    print('match')

print('--------------')

import re

word = 'mehe'
print(re.findall(r'^m..e$',word))
