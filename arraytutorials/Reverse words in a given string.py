'''Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i'''

def reverseWords(s):

    return '.'.join(s.split('.')[::-1])



print(reverseWords('i.like.this.program.very.much'))