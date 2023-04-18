'''Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.'''

def nonrepeatingCharacter(s):
    char_count = {}
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
            
    for i in s:
        if char_count[i] == 1:
            return i
    return None



print(nonrepeatingCharacter('hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs'))
