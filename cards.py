class card:
    def __init__(self, name, value, ace):
        self.name = name
        self.value = value
        self.ace = ace

def generate_deck():
    deck = []

    suits = ["Spades", "Clovers", "Hearts", "Diamonds"]

    cards = [
        ("A", 11, True),
        ("2", 2, False),
        ("3", 3, False),
        ("4", 4, False),
        ("5", 5, False),
        ("6", 6, False),
        ("7", 7, False),
        ("8", 8, False),
        ("9", 9, False),
        ("10", 10, False),
        ("J", 10, False),
        ("Q", 10, False),
        ("K", 10, False)
        ]

    for suit in suits:
        for name, value, ace in cards:
            card_name = (f"{name} of {suit}")
            deck.append(card(card_name, value, ace))

    return deck