contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()
for x in contacts:
    if name in x:
        print(str(x[0]) + ' is '+ str(x[1]))
        break
else:
    print("Not found")


## tupple unpacking
a, b , c, *d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)


##sets
num_set = {1,2,3,4,4}
num_set.add(-3)
num_set.remove(2)
print('num set',num_set)


a = {1}
b = {}
a.add(2)
b.add(2)
print(a&b)