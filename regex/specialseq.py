'''r'(abc|xyz) \1'   would match abc or xyz then the same thing again'''
import re
pattern = r'(.+)(.+)(.+) \1'

if re.match(pattern, '12 34 56 12'):
    print('match 1')
if re.match(pattern, '12 34 56 34'):
    print('match 2')
if re.match(pattern, '12 34 56 56'):
    print('match 3')

'''\A is an anchor that says "the string starts here" 
so in other words no characters may occur before \A 
\Z is an anchor that says "the string ends here" 
so in other words no characters may occur after \Z 
\b matches 1 or more spaces and 0 or more letters (words).
So in other words there must be at least 1 word to the left of \b and at least 1 word to the right of \b.'''

'''Sample Input
No #pressure, no #diamonds

Sample Output
#pressure
#diamonds'''



text = 'No #pressure, no #diamonds'

pick = r'#\w+'

print(re.findall(pick,text))