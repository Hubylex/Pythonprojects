# a word or phrase that reads \
# the same backwards

def check_palindrom(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return 'the following  text IS palindrome'
    else:
        return 'the following text IS  NOT palindrome'

print(check_palindrom(input('enter')))


