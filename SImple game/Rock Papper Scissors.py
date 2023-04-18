print('THIS IS A GAME OF ROCK PAPER SCISSORS')

def game(p1,p2):
    if p1 == p2:
        return ' It"s a draw'
    elif p1 == 'rock':
        if p2 == 'paper':
            return 'player 2 wins'
        else:
            return 'player 1 wins'
    elif p1 == 'paper':
        if p2 == 'scissors':
            return 'player 2 wins'
        else:
            return 'player 1 wins'
    elif p1 == 'scissors':
        if p2 == 'rock':
            return 'player 2 wins'
        else:
            return 'player 1 wins'
    else:
        return 'Invalid input: try entry rock/paper/scissors'

player_1 = input('PLAYER 1 ')
player_2 = input('PLAYER 2 ')

print(game(player_1,player_2))


