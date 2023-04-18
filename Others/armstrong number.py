def check_a(num):
    sum_d = 0
    for i in str(num):
        n = len(str(num))
        sum_d += int(i)**n
    if num == sum_d:
        return 'Number is an ARMSTRONG'
    else:
        return 'Number is NOT an ARMSTRONG'

print(check_a(int((input('enter')))))