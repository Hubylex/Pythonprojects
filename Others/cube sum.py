# for an n
# sum all cubes of numbers up to n

def sum_cubes(n):
    sum = 0
    for i in range(1,n+1):
        sum += (i**3)
    return sum
print(sum_cubes(int(input('enter'))))



### alternate approach
## using formula

def sum_cubes2(s):
    return (s*(s+1)/2)**2
print(sum_cubes2(int(input('enter'))))


## my other approach
def square(n):
    return sum([i**3 for i in range(n+1)])
print(square(int(input('enter'))))