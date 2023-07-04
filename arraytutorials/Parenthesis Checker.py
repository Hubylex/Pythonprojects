'''Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of 
unbalanced bracket.'''

def ispar(x):
    pairs = {
        '{':'}',
        '(':')',
        '[':']'
        }
    
    lt = int(len(x))
    l = int(len(x)/2)

    for i in x[:l]:
        if x.index(pairs[i])==(lt-1)-x.index(i):
            continue
        else:
            return False
        
    return True

print(ispar('{([])}'))






