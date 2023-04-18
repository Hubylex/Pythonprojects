import PySimpleGUI as sg
import random
layout = [
    [sg.Text('YOU GET 10 CHANCES TO GUESS THE LUCKY NUMBER')],
    [sg.Input(key='-input-'),sg.Button('Enter')],
    [sg.Text(key='-response-')]

]

window = sg.Window('GAME',layout)

while True:
    user_points = 0
    event,values = window.read()
    if event == sg.WIN_CLOSED:
            break
    if event=='Enter':
        user_input = values['-input-']
        lucky_number = random.randint(1,10)
        
        
        if int(user_input) == lucky_number:
                user_points += 10
                print('well guessed')
                print('TOTAL POINTS AQUIRED IS ',user_points)

        else:
                print('nah!!,wrong guess - lucky number was ',lucky_number)



window.close()