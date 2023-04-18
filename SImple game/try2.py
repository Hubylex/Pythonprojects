import PySimpleGUI as sg

layout = [
    [sg.Text('You have entered: '),sg.Text(key='-reply-')],
    [sg.Canvas(size=(150,150),background_color='white',pad=(100,0),key='-canvas-')]
]

window = sg.Window('my app',layout,finalize=True)

canvas = window['-canvas-'].TKCanvas

# Draw the horizontal grid lines
for i in range(0, 150, 50):
    canvas.create_line(0, i, 150, i, fill='black')

# Draw the vertical grid lines
for i in range(0, 150, 50):
    canvas.create_line(i, 0, i, 150, fill='black')


# Draw the numbers in the cells
for i in range(0, 150, 50):
    for j in range(0, 150, 50):
        # Calculate the center point of the cell
        x = j + 50 // 2
        y = i + 50 // 2

        # Calculate the cell number
        cell_num = (i // 50) * 3 + j // 50 + 1

        # Draw the cell number in the center of the cell
        canvas.create_text(x, y, text=str(cell_num))

# Define the function to handle clicks on the canvas
def handle_click(event):
    # Get the coordinates of the click
    x, y = event.x, event.y

    # Calculate the cell number that was clicked
    cell_col = x // 50
    cell_row = y // 50
    cell_num = cell_row * 3 + cell_col + 1

    # Display a message with the cell number
    window['-reply-'].update(cell_num)


# Bind the click event to the canvas
canvas.bind('<Button-1>', handle_click)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()