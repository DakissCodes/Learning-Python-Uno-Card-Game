"""" UNO CARD GAME PLAYER VS PLAYER
"""
from ctypes.wintypes import PLARGE_INTEGER
from gettext import Catalog
from hashlib import new
from pickletools import read_unicodestring1
import random
from sys import displayhook
class Cards():
    def __init__(self,color,card_type):
        self.color = color
        self.card_type = card_type

    def __str__(self):
        return f'{self.color} of {self.card_type}'

class Deck(Cards):
    
    colors = ['All','Red','Blue','Green','Yellow']
    card_type = ['Zero','One','Two','Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Skip','Reverse','DrawTwo']
    wild_card_type = ['Wild','WildDrawFour'] 
    def __init__(self):
        self.newdeck = []
        for _ in range(2):
            for x in self.colors[1:]:
                for y in self.card_type[1:]:
                    self.newdeck.append(Cards(x,y))
        for _ in self.colors[1:]:
            self.newdeck.append(Cards(_,self.card_type[0]))
        for _ in range(4):
            self.newdeck.append(Cards(self.colors[0],self.wild_card_type[0]))
            self.newdeck.append(Cards(self.colors[0],self.wild_card_type[1]))
    
    def deal_one(self):
        return self.newdeck.pop()

class Player(Deck,Cards):
    def __init__(self):
        self.player_one = []
        self.player_two = []


'''
#create a function that 

# function that checks whether drop card is compatible with top card
# if color or type == to that of top card, return false (set a bool to false)
# if not bool: create another check function that in order to be compatible
# type == topcard.card_type. 
# function works for: nums. if type is wild or draw, we break.
'''
'''
1st while: while True:
put if statements here, (if len(deck1) == 0: break. Game over!)

2nd while: while True:
This is player_one's turn. 
includes the ff:
1st - draw or drop?
if drop, asks the index of the card you want. 

(first checker allows color == color or type == type)
(second checker, [once bool is False], only allows if type==type)

NOTE: it continues asking for a card to drop until you enter stop,
which breaks the loop.
NOTE: ALL WILD AND DRAW CARDS BREAK THE WHILE LOOP.

2nd = if draw, pops from the deck, appends it to player one's deck.
then break.

3rd while loop: While True
just the same as 2nd while loop, but for the second player. 
'''

