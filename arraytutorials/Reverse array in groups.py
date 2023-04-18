'''Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.'''

def rev(arr,K):
    if len(arr)<=K:
        return arr[::-1]
    else:
        return arr[K-1::-1] + rev(arr[K:],K)

print(rev([1,2,3,4,5,6,3,4],3))