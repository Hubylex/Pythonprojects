def rev_num(nums):
    rev = ''
    while nums>0:
        last_digit = nums%10
        rev = rev + str(last_digit)
        nums = nums//10
    return rev

print(rev_num(int(input('enter'))))