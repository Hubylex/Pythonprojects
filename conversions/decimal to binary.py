def c(n):
    r = ''
    while n >= 1:
        d = n%2
        r += str(d)
        n = n//2
    return r[::-1]


print(c(9))
