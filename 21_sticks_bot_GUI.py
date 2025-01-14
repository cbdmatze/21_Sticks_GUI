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
    