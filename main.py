import random

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    dealt_cards = []
    for i in range(number):
        dealt_cards.append(cards.pop())
    return dealt_cards

shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]

if rank == "A":
    value = 11
elif rank == "J" or rank == "K" or rank == "Q":
    value = 10
else: 
    value = int(rank)

rank_dict = {"rank": rank, "value": value}

print(rank_dict["rank"], rank_dict["value"])