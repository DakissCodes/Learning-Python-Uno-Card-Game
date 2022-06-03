"""" UNO CARD GAME PLAYER VS PLAYER
"""
import random

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


def move_card(alldeck,deck,deck2,index,stash,comp):
    index = int(index) - 1
    card = comp[index]
    index2 = deck.index(card)
    if card.card_type == 'Skip' or card.card_type == 'Reverse':
        print('Your turn again!')
        stash.append(deck.pop(int(index2))) # CHANGE THIS: WE CAN USE deck,index(card)
        return 0

    elif card.card_type == 'DrawTwo':
        for _ in range(2): deck2.append(alldeck.pop())
        print('Player 2 has drawn 2 cards!\n')
        stash.append(deck.pop(int(index2)))
        return 1

    elif card.card_type == 'WildDrawFour':
        for _ in range(4): deck2.append(alldeck.pop())
        print('Player 2 has drawn 4 cards!\n')
        change_color = ''
        while change_color.lower() not in ['green','red','blue','yellow']:
            change_color = input('What color would you like to change to? :\n ')
        card.color = change_color.capitalize()
        stash.append(deck.pop(int(index2)))
        return 1

    elif card.card_type == 'Wild':
        change_color = ''
        while change_color.lower() not in ['green','red','blue','yellow']:
            change_color = input('What color would you like to change to? :\n ')
        card.color = change_color.capitalize()   
        stash.append(deck.pop(int(index2)))
        return 1
    
    else:
        stash.append(deck.pop(int(index2)))

def display(deck,stash_deck,comp_list):
    x = len(deck)
    print(f'THE TOP CARD: {stash_deck[-1]}\n')
    print('\n')
    print(f'YOUR CARDS ({x}) : ' +  ' , '.join([str(_) for _ in deck]))
    x = ' , '.join([str(_) for _ in comp_list])
    print('USE: ' + x)

def check_one(comp_cards_one,index,stash_deck,op):
    index = int(index) - 1
    op2 = True
    if index not in range(len(comp_cards_one)):
        op2 = False
        return False
    else:
        card = comp_cards_one[int(index)]
        face_card = stash_deck[-1]
    if op and op2:
        if card.color == 'All': 
            return True
        elif card.color == face_card.color:
            return True
        elif card.card_type == face_card.card_type:
            return True
        else:
            return False
    elif not op and op2:
        if card.card_type == face_card.card_type:
            return True
        else:
            return False
def comp_cards(deck1,stash,op):
    top_card = stash[-1]
    if op:
        comp_cards = [_ for _ in deck1 if _.color == top_card.color or _.card_type == top_card.card_type\
            or _.color == 'All']
    elif not op:
        comp_cards = [_ for _ in deck1 if _.card_type == top_card.card_type]
    return comp_cards


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

