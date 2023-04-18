text = input('enter text:')
def count(i):
    c = 0
    for a in text:
       if a == i:
           c += 1
    return c

dict = {i : count(i) for i in text}
print(dict)