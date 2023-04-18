

from itertools import count


def square(n):
    return sum([i**3 for i in range(n+1)])
print(square(3))

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

print([i for i  in range(20) if i%3 == 0])


text = 'hello'
def count(i):
    c = 0
    for a in text:
       if a == i:
           c += 1
    return c

dict = {(i , count(i)) for i in text}
print(list(dict))