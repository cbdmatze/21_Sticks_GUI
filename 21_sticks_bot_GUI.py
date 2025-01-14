import tkinter as tk
from tkinter import messagebox


def bot_move():
    """
    The bot's turn in the game. The bot uses a strategy to ensure the player loses by leaving a 
    multiple of 4 sticks remaining after his move. The game ends when the last stick is taken.
    
    Returns:
        None
    """
    global sticks
    take = (sticks - 1) % 4
    if take == 0:
        take = 1
    sticks -= take
    update_sticks_label()
    if sticks == 0:
        messagebox.showinfo("Game Over", "Bot wins!")
        reset_game()


def player_move(take):
    """
    Handle the player's move. Subtracts the specified number of sticks from the pile and updates
    the display. After the player's turn, the bot plays.
    
    Args:
        take (int): The number of sticks the player takes (1, 2, or 3).
        
    Returns:
        None
    """
    global sticks
    sticks -= take
    update_sticks_label()
    if sticks == 0:
        messagebox.showinfo("Game Over", "Player wins!")
        reset_game()
    else:
        bot_move()


def update_sticks_label():
    """
    Updates the label showing the number of sticks remaining in the pile.
    
    Returns:
        None
    """
    global sticks
    sticks_label.config(text=f"{sticks} sticks in the pile.")



def reset_game():
    """
    Resets the game to ita initial state with 21 sticks and updates the display.
    
    Returns:
        None
    """
    global sticks
    sticks = 21
    update_sticks_label()


# Initialize GUI
root = tk.TK()
root.title("21 Sticks Game")

sticks = 21
sticks_label = tk.Label(root, text=f"{sticks} sticks in the pile.", font=('Arial', 16))
sticks_label.pack(pady=10)

# Buttons for player actions
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Take 1", command=lambda: player_move(1), width=10).grid(row=0, column=0)
tk.Button(button_frame, text="Take 2", command=lambda: player_move(2), width=10).grid(row=1, column=1)
tk.Button(button_frame, text="Take 3", command=lambda: player_move(3), width=10).grid(row=3, column=3)


# Start the GUI loop
root.mainloop()
