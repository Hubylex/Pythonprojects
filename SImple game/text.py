import PySimpleGUI as sg
layout = [
    [sg.Input(key='text')],
    [sg.Button('enter'),sg.Text(key='reply1')],
    [sg.Text(key='reply2')]
    
]

window = sg.Window('yehh',layout)

while True:
    event ,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    for i in range(5):
        if event != 'enter':
            break
        continue
    print(values['text'])
        
window.close()