'''Given an unsorted array Arr of size N of positive integers. 
One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. 
Find these two numbers.

Input:
N = 6
Arr[] = {6,1,4,3,2,1}
Output: Missing = 5, Repeating = 1
Explanation: Repeating number is 1 and 
smallest positive missing number is 5.'''

def findTwoElement(arr): 
    d = []
    for i in range(len(arr)):
        if i not in  arr:
            missing = i
    for s in arr:
        if s not in d:
            d.append(s)
        else:
            r = s
        
 
        
    return f'missing: {missing}, repeating: {r}'
arr = [6,1,4,1,3,2]
print(findTwoElement(arr))


