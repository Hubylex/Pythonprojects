'''Input: S="geeksforgeeks"
Output: e'''

def rep(text):
    new = {}
    for i in text:
        c = 1
        if i in new:
           new[i] += c
        else:
            new[i] = c
        if new[i]==2:
            return i
    return 'No repeated character'

text = 'geeksforgeeks'
print(rep(text))