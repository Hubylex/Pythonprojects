'''Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.'''

def arrLeader(arr):
    for i in range(len(arr)):
        if arr[i]>=sum(arr[i+1:]):
            yield arr[i]

for s in arrLeader([63, 70, 80, 33, 33, 47, 20]):
    print(s,end=' ')
print('\n'+str(80>33+33+47+20))