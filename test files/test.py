def average():
    total_avg = 0
    rep = int(input('count of nums'))
    for i in range(0,rep):
         a = int(input('enter nums'))
         avg = a/(rep)
         total_avg += avg
    return total_avg
print('average is ',average())

