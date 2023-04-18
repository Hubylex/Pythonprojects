#ask user to enter a number\
#find all prime numbers up to that number

def prime(n):

    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True 

prime_list = []
def add_prime(n):
    for i in range(2,n+1):
        if prime(i) is True:
            prime_list.append(i)
    return prime_list

print(add_prime(int(input('enter'))))
        

