nums = {1,2,3,4,5,6}
print(nums)

nums = {0,1,2,3} & nums
print(nums)
nums = filter(lambda x:x>1,nums)
print(nums)
print(len(list(nums)))

print('---------')
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

print('---------')
a = (lambda x:x*(x+1))(6)
print(a)

print('---------')
nums = [1,2,8,3,7]
res = list(filter(lambda x:x%2 == 0,nums))
print(res)

print('---------')
def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)

