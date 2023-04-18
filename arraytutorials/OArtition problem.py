'''The partition problem is to determine whether a given set can be partitioned into two subsets
 such that the sum of elements in both subsets is the same. 

Examples: 

Input: arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}'''


def checkpart(arr):
    for i in range(len(arr)):
        j = i+1
        if arr[i]==sum(list(filter(lambda x:x != arr[i],arr))):
            return True,arr[i],list(filter(lambda x:arr.index(x) != i,arr))
        if sum([arr[i],arr[j]]) == sum(list(filter(lambda x:x != arr[i]and x!=arr[j],arr))):
            return True,[arr[i],arr[j]],list(filter(lambda x:arr.index(x) != i and arr.index(x) != j,arr))
        
    return False
print(checkpart([1, 5, 11, 5]))