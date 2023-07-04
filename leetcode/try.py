def isValid(s):
    pairs = {
        '{':'}',
        '(':')',
        '[':']'
        }
    
    for i in s:

        
        if i in pairs.values():

            continue
        elif s.index(pairs[i]) - s.index(i)%2!=0:
            continue
        else:
            return False,i
    return True

print(isValid('()[]{}'))