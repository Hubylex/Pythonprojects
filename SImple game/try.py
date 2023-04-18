# import PySimpleGUI as sg

# # Define the layout for the window
# layout = [[sg.Canvas(size=(300, 300), background_color='white', key='-CANVAS-')]]

# # Create the window with the finalize parameter
# window = sg.Window('Grid Example', layout, finalize=True)

# # Get the canvas element from the window
# canvas = window['-CANVAS-'].TKCanvas

# # Define the grid line spacing
# spacing = 50

# # Draw the horizontal grid lines
# for i in range(0, 300, spacing):
#     canvas.create_line(0, i, 300, i, fill='black')

# # Draw the vertical grid lines
# for i in range(0, 300, spacing):
#     canvas.create_line(i, 0, i, 300, fill='black')

# # Event loop
# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break

# # Close the window
# window.close()



import PySimpleGUI as sg

# Define the layout for the window
layout = [[sg.Canvas(size=(300, 300), background_color='white', key='-CANVAS-')]]

# Create the window with the finalize parameter
window = sg.Window('Grid Example', layout, finalize=True)

# Get the canvas element from the window
canvas = window['-CANVAS-'].TKCanvas

# Define the grid line spacing and cell size
spacing = 50
cell_size = 30

# Draw the horizontal grid lines
for i in range(0, 300, spacing):
    canvas.create_line(0, i, 300, i, fill='black')

# Draw the vertical grid lines
for i in range(0, 300, spacing):
    canvas.create_line(i, 0, i, 300, fill='black')

# Draw the numbers in the cells
for i in range(0, 300, spacing):
    for j in range(0, 300, spacing):
        # Calculate the center point of the cell
        x = i + spacing // 2
        y = j + spacing // 2

        # Calculate the cell number
        cell_num = (i // spacing) * 3 + j // spacing + 1

        # Draw the cell number in the center of the cell
        canvas.create_text(x, y, text=str(cell_num))

# Define the function to handle clicks on the canvas
def handle_click(event):
    # Get the coordinates of the click
    x, y = event.x, event.y

    # Calculate the cell number that was clicked
    cell_col = x // spacing
    cell_row = y // spacing
    cell_num = cell_row * 3 + cell_col + 1

    # Display a message with the cell number
    sg.popup(f'Clicked cell {cell_num}')

# Bind the click event to the canvas
canvas.bind('<Button-1>', handle_click)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

# Close the window
window.close()
