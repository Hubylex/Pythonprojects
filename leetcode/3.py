# a=1,2,3,7,5
# s=12   n=5
arr = [1,2,3,4,5,6,7,8,9,10]


def subarray(arr,n,s):
    
    summ = {}
    t = {}
    for i in range(n+1):
        for j in range(i+1,n+1):
            summ[i,j] = sum(arr[i:j])
    for (x,y) in summ:
        if summ[x,y] == s and x+1!=y:
           return x+1,y
    return -1
print(subarray(arr,10,15))

