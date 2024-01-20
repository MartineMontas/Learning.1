import random


card_deck = []


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def play(self):
        if self.rank == 1:
            self.rank = "Ace"
        elif self.rank == 11:
            self.rank = "Jack"
        elif self.rank == 12:
            self.rank = "Queen"
        elif self.rank == 13:
            self.rank = "King"

        if self.suit == 1:
            self.suit = "Spades"
        elif self.suit == 2:
            self.suit = "Diamonds"
        elif self.suit == 3:
            self.suit = "Hearts"
        elif self.suit == 4:
            self.suit = "Clubs"

        print("{} of {}".format(self.rank, self.suit))


def initialize(cards):
    for rank in range(1, 14):
        for suit in range(rank, 5):
            cards = Card(rank, suit)
            card_deck.append(cards)


def shuffle(cards):
    for i in range(0, len(cards)):
        destination = random.randint(0, len(cards) - 1)
        temp = cards[destination]
        cards[destination] = cards[i]
        cards[i] = temp


def print_set(cards):
    print("Printing Cards")
    for i in range(0, 5):
        card_deck[i].play()


def main():
    initialize(card_deck)
    shuffle(card_deck)
    print_set(card_deck)


if __name__ == "__main__":
    main()
