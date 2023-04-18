import random
print('YOU GET 10 CHANCES TO GUESS THE LUCKY NUMBER')
user_points = 0

for i in range(10):
    lucky_number = random.randint(1,10)

    user_input = input('GUESS THE NUMBER:')

    if   user_input =='q':
               confirmation = input('ARE YOU SURE YOU WANT TO QUIT \n YES OR NO')
               if confirmation == 'YES':
                  print('MATCH HAS BEEN TERMINATED') 
                  print('TOTAL POINTS AQUIRED IS ',user_points) 
                  break

    elif int(user_input) == lucky_number:
               user_points += 10
               print('well guessed')
               print('TOTAL POINTS AQUIRED IS ',user_points)

    else:
              print('nah!!,wrong guess - lucky number was ',lucky_number)


## computer submmited

import random
 
secret_number = str(random.randint(1000, 9999))
print("Guess the number. It contains 4 digits.")
 
remaining_try = 7
 
def get_bulls_cows(number, user_guess):
    bulls_cows = [0,0] #cows, then bulls
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls_cows[0] += 1
        elif user_guess[i] in number:
            bulls_cows[1] += 1
    return bulls_cows
 
while remaining_try > 0:
    player_guess = input("Enter your guess: ")
  
    if player_guess == secret_number:
        print("Yay, you guessed it!")
        print("YOU WIN.")
        break
    else:
        bulls_cows = get_bulls_cows(secret_number,player_guess)
      
        print("Bulls: ",bulls_cows[0])
        print("Cows: ",bulls_cows[1])
 
        remaining_try -= 1
 
        if remaining_try < 1:
            print("You lost the game.")
            break
