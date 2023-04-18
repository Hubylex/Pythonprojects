def rev(txt):
    revers = ''
    for char in txt:
        revers = char + revers
    return revers

print(rev(input('enter')))


## shortest approach for reversing string
def rev2(txt):
    return txt[::-1]
print(rev(input('enter')))