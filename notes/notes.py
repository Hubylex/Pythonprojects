#dictionary repesentation
#key : value
ages = {
    'a': 2,
    'b': 1,
    'c': 0
}

print(ages['a'])
print(ages['b'])

#merging tw0 lits

k = [1,2,3,4]
v = [5,6,7,8]
s = [9,0]
merge = dict(zip(k,v))
print(merge)

## dictionary funstions
ages = {
    'huby' : 'lex',
      12   : 24,
    'jilak' : 19,
    'huby' : 'me'

}

print(ages['huby'])
print(ages[12])
print('huby' in ages)
print(4 not in ages)

print(len(ages))