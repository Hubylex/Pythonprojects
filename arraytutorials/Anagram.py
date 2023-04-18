'''Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with
        same frequency. So, both are anagrams.'''

def isAnagram(a,b):
    a_data = {}
    b_data = {}
    for i in a:
        if i not in a_data:
            a_data[i]=1
        else:
            a_data[i] += 1
    for i in b:
        if i not in b_data:
            b_data[i]= 1
        else:
            b_data[i]+=1
    for i in a_data:
            if a_data.get(i)==b_data.get(i) and len(a)==len(b):
                continue
            else:
                return False


print(isAnagram('uths','uxws'))

    
