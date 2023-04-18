# def letter_check(letter):
#     vowels = ['a','e','i','o','u']
    
#     if letter in vowels:
#         return f'{letter} is a vowel'
#     elif letter == 'y':
#         return 'y may be a  vowel or a consonant'
#     else:
#         return f'{letter} is a consonant'
# letter = input('Enter a single letter')
# print(letter_check(letter))


# def pig_latin(text):
#     v = ['a','e','i','o','u']
#     if text[0] not in v:
   
#         for i in text:
#             if i not in v:
#                 text =  text.replace(i,'') + i
#             else:
#                 break
#         return text + 'ay'
#     else:
#         return text + 'way'

# print(pig_latin('hubert'))

def c(values):
    if values[0] ==' ':
        return 0.0
    else:
        return 1 + c(values[1:])

print(c(' '))

def eucl(a,b):
    if b==0:
        return a
    else:
        return eucl(b,a%b)
    
print(eucl(45,5))


# def avg():
#     print('Enter values \nEnter zero to mark end')
#     a = 1
#     s = 0
#     i = 0
#     while a != 0:
#         a = int(input())
#         s += a
#         i+=1
#     print(s/(i-1))

# avg()


