import re
str = "Please contact Me.lastname@tafe.com for assistance"

mail =r"([\w\.-]+)@([\w\.-]+)([\.\w-])"


match=  re.search(mail,str)
if match:
    print(match.group())