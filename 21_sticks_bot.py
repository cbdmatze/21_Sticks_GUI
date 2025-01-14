def bot_plays_21_sticks():
    """
    Play the 21 sticks game with a bot (Player 1) and a human player (Player 2).
    The bot ensures that Player 2 will lose by always leaving a multiple of 4 sticks for the player.
    The game ends when the last stick is taken.
    
    Returns:
        None
    """
    sticks = 21
    player_turn = 1 # Player 1 (bot) starts

    print("21 sticks in the pile.")

    while sticks > 0:
        if player_turn == 1:
            # Bot's strategy: leave a multiple of 4 sticks
            take = (sticks - 1) % 4
            if take == 0:
                take = 1 # If already a multiple of 4, take 1
                print(f"Bot takes: {take}")
            else:
                print("Player takes: ", end="")
                take = int(input()) # User input

            # Subtract the number of sticks taken
            if sticks > 0:
                print(f"{sticks} sticks in the pile")
            else:
                print("0 sticks in the pile")

            # Check if someone won
            if sticks == 0:
                if player_turn == 1:
                    print("Bot won!")
                else:
                    print("Player won!")
                break

            # Switch turns
            player_turn = 2 if player_turn == 1 else 1


# Run the game with the bot
bot_plays_21_sticks()
