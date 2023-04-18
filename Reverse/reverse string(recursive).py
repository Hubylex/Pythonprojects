def rev_str(str):
    if len(str) == 0:
        return str
    else:
        return rev_str(str[1:]) + str[0]
print(rev_str(input('enter')))