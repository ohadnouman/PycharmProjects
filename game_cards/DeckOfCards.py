import random

from card import *

class DeckOfCards:

    def __init__(self):
        self.list_cards=[]
        for i in range(1,14):
            for j in range(1,5):
                card=Card(i,j)
                self.list_cards.append(card)
                print(self.list_cards)

    def cards_shuffle(self):
        random.shuffle(self.list_cards)

    def deal_one(self):
        card_random=random.choice(self.list_cards)









