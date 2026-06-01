from cards import generate_deck
from random import randrange

import random

def game(player_money):
    while True:
        player_bet = int(input("How much would you like to bet? "))
        if player_bet > player_money:
            print("Woa there buddy, you don't have that much moolah.")
        else:
            break
    
    deck = generate_deck()
    player_hand = []
    dealer_hand = []
    deal_cards(player_hand, dealer_hand, deck)
    while True:
        print(render_screen(player_hand, dealer_hand, False))
        response = prompt()
        if response == True:
            add_card(player_hand, deck)
            if count(player_hand) > 21:
                result = ace_check(player_hand)
                if result == "no-aces":
                    break
            elif count(player_hand) == 21:
                break
        elif response == False:
            break
        
    result = showdown(player_hand, dealer_hand, player_bet, deck)
    return result


def prompt():
    response = 0
    while True:
        response = int(input("Would you like to hit [1] or stay [2] "))
        if response == 1:
            return True
        elif response == 2:
            return False
        else:
            print("Invalid input. Please follow the very clear instructions.")

def deal_cards(player_hand, dealer_hand, deck):
    for _ in range(2):
        add_card(dealer_hand, deck)
        add_card(player_hand, deck)

def add_card(person_cards, deck):
    random_card = random.randrange(len(deck))
    person_cards.append(deck[random_card])
    deck.pop(random_card)
    
def count(hand):
    count = 0
    for card in hand:
        count += card.value
    return count

def showdown(player_hand, dealer_hand, player_bet, deck):
        if count(player_hand) > 21:
            print(render_screen(player_hand, dealer_hand, True))
            return player_loss(player_bet)

        while True:
            if count(dealer_hand) >= 16:
                if count(dealer_hand) > count(player_hand):
                    print(render_screen(player_hand, dealer_hand, True))
                    return player_loss(player_bet)
                elif count(dealer_hand) < count(player_hand):
                    print(render_screen(player_hand, dealer_hand, True))
                    return player_victory(player_bet)
                elif count(dealer_hand) == count(player_hand):
                    return draw()
                
            add_card(dealer_hand, deck)
            print(render_screen(player_hand, dealer_hand, True))

            if count(dealer_hand) > 21:
                result = ace_check(dealer_hand)
                if result == "no-aces":
                    return player_victory(player_bet)
        
    


def render_screen(player_hand, dealer_hand, showdown):
        if showdown == True:
            player_score = count(player_hand)
            dealer_score = count(dealer_hand)
            player_cards = ""
            dealer_cards = ""
            for card in dealer_hand:
                dealer_cards += card.name
                dealer_cards += ","
            for card in player_hand:
                player_cards += f"{card.name}"
                player_cards += ","

            return f"""
            Dealer: [{dealer_score}], {dealer_cards}
            You: [{player_score}] {player_cards}
            """
        else:
            player_score = count(player_hand)
            dealer_score = dealer_hand[0].value
            player_cards = ""
            dealer_card = dealer_hand[0].name
            for card in player_hand:
                player_cards += f"{card.name}"
                player_cards += ","

            return f"""
            Dealer: [{dealer_score}], {dealer_card}, ###
            You: [{player_score}] {player_cards}
            """
        
def player_loss(player_bet):
    print("You lost... bummer")
    return ("player_loss", player_bet)

def player_victory(player_bet):
    print("You Won!")
    return ("player_victory", player_bet)

def draw():
    print("draw.")

def ace_check(hand):
    for card in hand:
        if card.ace == True:
            card.value = 1
            card.ace = False
            return
    return "no-aces"