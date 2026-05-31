import game_functions
chips = 100

while True:
    print("Welcome to BlackJack!")
    print(f"You currently have: {chips} chips!")
    input("Please enter any key to start the game.")
    game = game_functions.game(chips)
    if game[0] == "player_victory":
        chips += game[1]
    else:
        chips -= game[1]