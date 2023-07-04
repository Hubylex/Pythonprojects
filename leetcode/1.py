'''Given a string s, find the length of the longest 
substring
 without repeating characters.
 
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

def lengthOfLongestSubstring(s):
    subb = {}
    sub = ''
    for i in range(len(s)):
        if s[i] not in sub:
            sub += s[i]
        
        elif (s[i] not in sub) and (s[i-1] in sub):
            subb['1'] = sub
            sub = ''
            sub += s[i]

        else:
            continue

    return subb,sub
    
print(lengthOfLongestSubstring('abcabcbfrteb'))


a = {
    1:'one'
}
a[2]='two'
print(a)