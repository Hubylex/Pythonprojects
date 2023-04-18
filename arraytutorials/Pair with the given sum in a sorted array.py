'''Given a sorted array and a number x, find a pair in an array whose sum is closest to x.

Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10'''






def pair(arr,x):
    sums = {}
    for i in range(len(arr)):
      j = i+1
      while  j<len(arr):
        add = arr[i] + arr[j]
        sums[arr[i],arr[j]] = abs(x-add)
        j+=1
    for i in range(len(arr)):
      j = i+1
      while  j<len(arr):
        add = arr[i] + arr[j]
        if abs(x-add)== min(sums.values()) :
            return arr[i],arr[j]
        j+=1
    


print(pair([1, 3, 4, 7, 10],15))
