import random
import string

def pass_word(length):
    password = ''
    all_chars = string.ascii_letters + string.digits + string.punctuation
    while len(password) < length :
         rand_char = random.choice(all_chars)
         password += rand_char
    return password

create_password = pass_word(7)
print('Your password is :',create_password)




