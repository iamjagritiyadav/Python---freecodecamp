import random

# -----------------------------
# Card Class
# -----------------------------
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


# -----------------------------
# Deck Class
# -----------------------------
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"
        ]

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


# -----------------------------
# Hand Class
# -----------------------------
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.card_value(card)

        if card.value == "Ace":
            self.aces += 1

        self.adjust_for_ace()

    def card_value(self, card):
        if card.value in ["Jack", "Queen", "King"]:
            return 10
        elif card.value == "Ace":
            return 11
        else:
            return int(card.value)

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# -----------------------------
# Game Logic
# -----------------------------
def show_hand(player, hand):
    print(f"\n{player}'s hand:")
    for card in hand.cards:
        print(card)
    print(f"Value: {hand.value}")


def blackjack():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # Initial deal
    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    show_hand("Player", player_hand)
    show_hand("Dealer", dealer_hand)

    # Player turn
    while player_hand.value < 21:
        choice = input("\nHit or Stand? (h/s): ").lower()
        if choice == "h":
            player_hand.add_card(deck.deal())
            show_hand("Player", player_hand)
        else:
            break

    if player_hand.value > 21:
        print("\nPlayer busts! Dealer wins.")
        return

    # Dealer turn
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal())

    show_hand("Dealer", dealer_hand)

    # Result
    if dealer_hand.value > 21:
        print("\nDealer busts! Player wins.")
    elif dealer_hand.value > player_hand.value:
        print("\nDealer wins.")
    elif dealer_hand.value < player_hand.value:
        print("\nPlayer wins!")
    else:
        print("\nIt's a tie!")


# -----------------------------
# Testing Game
# -----------------------------
if __name__ == "__main__":
    blackjack()
