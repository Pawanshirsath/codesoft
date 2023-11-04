import tkinter as tk
from tkinter import messagebox
import random

# Create a 3x3 grid for the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Initialize the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the Tic-Tac-Toe grid
buttons = [[None, None, None] for _ in range(3)]

# Create a variable to keep track of the current player
current_player = 'X'

# Create a function to handle button clicks
def button_click(row, col):
    if board[row][col] == ' ':
        update_board(row, col)
        draw_board()
        if check_win(current_player):
            end_game(f'{current_player} wins!')
        elif check_draw():
            end_game("It's a draw!")
        else:
            switch_player()
            ai_move()

# Create a function to update the board
def update_board(row, col):
    board[row][col] = current_player

# Create a function to draw the board
def draw_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                buttons[i][j].config(text='X', state='disabled')
            elif board[i][j] == 'O':
                buttons[i][j].config(text='O', state='disabled')

# Create a function to check for a win
def check_win(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Create a function to check for a draw
def check_draw():
    return all(cell != ' ' for row in board for cell in row)

# Create a function to end the game
def end_game(message):
    messagebox.showinfo("Game Over", message)
    root.quit()

# Create an AI opponent
def ai_move():
    if current_player == 'O':
        return

    # You can implement the AI move strategy here.
    # For a simple example, let's make a random move.
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        update_board(row, col)
        draw_board()
        if check_win(current_player):
            end_game(f'{current_player} wins!')
        elif check_draw():
            end_game("It's a draw!")
        else:
            switch_player()

# Create a function to switch players
def switch_player():
    global current_player
    current_player = 'X' if current_player == 'O' else 'O'

# Create and configure buttons in the GUI
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', width=10, height=3,
                                  command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Start the game
root.mainloop()
