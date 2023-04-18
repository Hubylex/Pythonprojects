'''def  firstElementKTime( a, n, k):
    nums = {}
    for i in range(n):
        c = 0
        for s in a:
            if a[i] == s:
                c += 1
                nums[a[i]]= c

    return nums     


print(firstElementKTime([1,3,7,4,7,3,7,8,7],9,2))'''

def firstElementKTime(a, n, k):
    nums = {}
    for i in range(n):
        if a[i] in nums:
           nums[a[i]] += 1
        else:
            nums[a[i]] = 1
        if nums[a[i]] == k:
             return a[i]
    return -1
                       
                        
    
print(firstElementKTime([2,5,3,2,2],5,3))