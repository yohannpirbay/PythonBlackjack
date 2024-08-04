import random

class Deck():

    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},  
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]
    
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        dealt_cards = []
        for i in range(number):
            if len(self.cards) > 0:
                dealt_cards.append(self.cards.pop())
        return dealt_cards
    
deck_one = Deck()
deck_two = Deck()
deck_one.shuffle()
print(deck_one.deal(1))
print(deck_two.deal(1))