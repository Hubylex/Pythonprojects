import random
holy_num = str(random.randint(1000,9999))

tries = 7

    

def game(user_num,holy_num):
   
    bull_cow = [0,0]

    for i in range(4) :
        if user_num[i] == holy_num[i]:
            bull_cow[0] += 1
        elif user_num[i] in holy_num:
            bull_cow[1] += 1
    
    return bull_cow

while tries > 0:
    user_num = input('enter four digit number')
    if user_num == holy_num:
        print('YOU GUESSED RIGHT')
        print('YOU WIN')
        break
    else:
        bull_cow = game(user_num,holy_num)
        print('bulls: ',bull_cow[0])
        print('cow: ',bull_cow[1])
        tries-=1

        if tries == 1:
            print('YOU LOOSE')
            print('THE NUMBER WAS ',holy_num)

print(holy_num)
        


