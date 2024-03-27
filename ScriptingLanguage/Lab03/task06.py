import random


def deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    deck_of_cards = [(rank, suit) for rank in ranks for suit in suits]
    return deck_of_cards


def shuffle_deck(deck):
    shuffled_deck = deck[:]  # Make a copy of the original deck
    random.shuffle(shuffled_deck)
    return shuffled_deck


def deal(deck, n):
    if len(deck) < 5 * n:
        print("Not enough cards in the deck to deal to all players.")
        return None

    dealt_hands = []
    for i in range(n):
        hand = []
        for j in range(5):
            hand.append(deck.pop())
        dealt_hands.append(hand)

    return dealt_hands


# Test
my_deck = deck()
shuffled_deck = shuffle_deck(my_deck)
hands = deal(shuffled_deck, 4)

print("Okey lets goooo")
for i, player_hand in enumerate(hands, start=1):
    print(f"Player {i} hand:")
    for card in player_hand:
        print(f"{card[0]} {card[1]}")
    print()