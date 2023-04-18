'''* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.'''

import re

pattern = r'huby(lex)*'

if re.match(pattern,'huby'):
    print('Match 1')
if re.match(pattern,'hubylexxy'):
    print('Match 2')
if re.match(pattern,'lexxyhuby'):
    print('Match 3')

# this matches string that start wtih huby followed by lex or just huby


pattern = r'huby(lex)+'

if re.match(pattern,'huby'):
    print('Match x')
if re.match(pattern,'hubylexxy'):
    print('Match y')
if re.match(pattern,'lexxyhuby'):
    print('Match z')


import re

pattern = r"^a(g)+" 
if re.match(pattern, "aga"): 
    print("Match +1") 
if re.match(pattern, "abcg"):
     print("Match +2") 
if re.match(pattern, "a"):
     print("Match +3") 
if re.match(pattern, "gggabc"): 
    print("Match +4")
pattern = r"^a(g)*" 
if re.match(pattern, "aga"): 
    print("Match *1") 
if re.match(pattern, "abcg"):
     print("Match *2") 
if re.match(pattern, "a"):
     print("Match *3") 
if re.match(pattern, "gggabc"):
     print("Match *4")