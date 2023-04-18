def rev_stack(txt):
    stack = []
    for char in txt:
        stack.append(char)

    rev = ''
    while len(stack) >0:
       last = stack.pop()
       rev = rev + last

    return rev

print(rev_stack(input('enter')))

## create a list/stack
# add all characters of text/input into stack
#get last  digit of stack(repeatedly)
#add dem to the string rev