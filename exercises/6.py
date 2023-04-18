import re 
pattern = r"[A-Z][A-Z][0-9]" 
search1 = re.search(pattern, "LS8") 
search2 = re.search(pattern, "E3") 
search3 = re.search(pattern, "AC130") 
if search1: 
    print("Match 1", search1.group()) 
if search2: 
    print("Match 2", search2.group()) 
if search3: 
    print("Match 3", search3.group())

    '''[a-z]: 1 lower case letter [A-Z]: 1 upper case letter 
    [A-Z]{3}: 3 consecutive upper case letters
     [A-Z]{3}[a-z][A-Z]{3}: 3 upper case letters + 1 lower case letter + 3 upper case letters 
     [^A-Z]: any character BUT an upper case letter
      [^A-Z]+: at least one such character
       [^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+: something else before and after our patter(AAAbCCC) 
       so there's no more than 3 consecutive upper case letters on each side'''