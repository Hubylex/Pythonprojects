def gcf(a,b):
    a_fac = {0}
    b_fac = {0}
    for i in range(1,a+1):
        if (a%i) == 0:
            a_fac.add(i)
    for i in range(1,b+1):
        if (b%i) == 0:
            b_fac.add(i) 

    return max(a_fac & b_fac)
print(gcf(5,10))


##alternate approach 
def gcff(a,b):
    small = min(a,b)
    gcd  = 1
    for i in range(1,small+1):
        if (a%i)==0 and (b%i)==0:
            gcd = i
    return small


print(gcff(5,10))

