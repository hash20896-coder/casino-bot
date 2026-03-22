# Simple Poker Game

import random

class Poker:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [(value, suit) for suit in suits for value in values]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

    def show_hands(self):
        print(f'Player hand: {self.player_hand}')
        print(f'Dealer hand: {self.dealer_hand}')

if __name__ == '__main__':
    game = Poker()
    game.shuffle_deck()
    game.deal()
    game.show_hands()