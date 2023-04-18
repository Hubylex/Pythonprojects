# second largest number of list


list = []
max = float('-inf')
second_last = float('-inf')
for x in list:
    if x > max:
        second_last = max
        max = x
    elif x > second_last and x != max:
        second_last = x

print(second_last)


