list = [64,34,25,12,22,11,90]
n = len(list)
for j in range(n):
  for i in range(n-1):
    if list[i]>list[i+1]:
        temp = list[i]
        list[i]= list[i+1]
        list[i+1]=temp
print(list)