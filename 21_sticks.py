def play_21_sticks():
    """
    Play the 21 sticks game with two players taking turns. The game starts with 21 sticks,
    and each player takes 1 to 3 sticks per turn. The game ends when the last stick is taken.
    Player 1 starts first.
    
    Returns:
        None
    """
    sticks = 21
    player_turn = 1 # Player 1 starts

    print("21 sticks in the pile.")

    while sticks > 0:
        print(f"Player {player_turn} takes: ", end="")
        take = int(input()) # Assuming valid input (1-3)

        # Subtract the number of sticks taken
        sticks -= take

        # Display remaining sticks
        if sticks > 0:
            print(f"{sticks} sticks in the pile.")
        else:
            print("0 sticks in the pile.")
        
        # Check if someone won
        if sticks == 0:
            print(f"Player {player_turn} won!")
            break

        # Switch players
        player_turn = 2 if player_turn == 1 else 1


# Run the game
play_21_sticks()
