#TODO Add exception handling.
import game_functions
import time
import sys
chips = 100
print("Welcome to BlackJack!")


while True:
    if chips == 0:
        print("awwweee you have no money...")
        time.sleep(2)
        print("get out.")
        time.sleep(0.5)
        sys.exit(0)

    print(f"You currently have: {chips} chips!")
    input("Please enter any key to start the game.")
    game = game_functions.game(chips)
    if game[0] == "player_victory":
        chips += game[1]
    else:
        chips -= game[1]