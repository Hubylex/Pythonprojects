'''Input:
N = 5
A[] = {1,2,5,4,0}
B[] = {2,4,5,0,1}
Output: 1
Explanation: Both the array can be 
rearranged to {0,1,2,4,5}'''

def check(arr1,arr2,N):
    arr1.sort()
    arr2.sort()
    for i in range(N):
        if arr1[i]!=arr2[i]:
            return 'Non-equal arrays'
    return 'Equal arrays'

print(check([2,1,3,5,4],[5,3,1,2,4],5))