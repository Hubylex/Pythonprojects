# check prime number
def num_check(n):
    for i in range(2,n):
       if n % i==0:
          return False
    return True

num = num_check(int(input('enter:')))
if num:
    print('prime')
else:
    print('not prime')
