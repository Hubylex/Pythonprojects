def isValid(s):                                                     #"()[]{}"          "(]"
    parenthesis = {
        '{':'}',
        '(':')',
        '[':']',
    }


    for i in s:
        if i in parenthesis.values():
            continue
        if parenthesis[i] in s :
           continue
        # elif pa:
            
        else:
            return False
        
    return True
            
print(isValid('()[]{}'))