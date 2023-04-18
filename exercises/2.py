import re 
pattern = r"123([0-9])*456" 
if re.match(pattern, "123456"): 
    print("Match 1")
if re.match(pattern, "123000000000456"): 
    print("Match 2") 
if re.match(pattern, "1230456"): 
    print("Match 3") 
if re.match(pattern, "123333444456"): 
    print("Match 4") 
if re.match(pattern, "12356"): 
    print("Match 5")