


# 🪵 21 Sticks Game 🪵



## Overview

This is a Python implementation of the classic 21 sticks game, where two players take turns to remove 1, 2, or 3 sticks from a pile of 21 sticks. The player forced to take the last stick wins. This project includes both a **Command-Line Version** and a **Graphical User Interface (GUI)** version powered by Tkinter, as well as a **Bot** that guarantees a win if it plays first.



## Features

- **Two-Player Mode**: Play with a friend in the command-line version.
- **Bot Mode**: The bot (Player 1) uses a strategy to always win.
- **GUI Mode**: A simple Tkinter-based interface for a more interactive experience.
  


## Game Rules

- There are 21 sticks in a pile.
- Players take turns to pick 1, 2, or 3 sticks.
- The player forced to take the last stick wins.



## How to Play

### Command-Line Version

1. Clone or download the repository.

2. Run the following command for the two-player game:

   ```bash
   python3 21_sticks.py
   ```

3. For the bot version (Player 1 is the bot):

   ```bash
   python3 bot_21_sticks.py
   ```



### GUI Version

1. Run the GUI version using:

   ```bash
   python3 gui_21_sticks.py
   ```

2. In the GUI, click on the buttons to take 1, 2, or 3 sticks. The bot will automatically make its move after each player turn.



## Strategy (Bot Version)

The bot uses a **winning strategy** to guarantee a victory by always leaving the player with a number of sticks that is a multiple of 4.

## Dependencies

- **Python 3.x**
- **Tkinter** (for the GUI version, included with standard Python installations)

## Example

### CLI Bot Version:

```bash
21 sticks in the pile.
Bot takes: 1
20 sticks in the pile.
Player takes: 3
17

