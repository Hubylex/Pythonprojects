#ask user to enter a number 
# find all the prime factors for that number

def p_factor(n):
    p_list = []
    for i in range(1,n+1):
        if (n%i) == 0:
            p_list.append(i)
    return p_list

print(p_factor(int(input('enter'))))
    


