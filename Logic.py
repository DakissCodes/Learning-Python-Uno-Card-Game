import os


import random
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from xml.dom.expatbuilder import FragmentBuilderNS
from Classes import Deck,Cards,Player



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



game = False


mydeck = Deck()
random.shuffle(mydeck.newdeck)
player_one = Player()
player_two = Player()
stash = []
for _ in range(5):

    player_one.player_one.append(mydeck.deal_one())
    player_two.player_two.append(mydeck.deal_one())

stash.append(mydeck.deal_one())
while True:

    if len(player_one.player_one) == 0:
        print('PLAYER ONE HAS WON THE GAME!')
        break
    elif len(player_two.player_two) == 0:
        print('PLAYER TWO HAS WON THE GAME!')
        break

    else:

        op = True
        draw = True

        while True:
            os.system('cls')


            comp_cards_one = comp_cards(player_one.player_one,stash,op)
            display(player_one.player_one,stash,comp_cards_one) # display mycards, and the top card
            drop_card_index = input('PLAYER 1 : What card to drop? [index] or [draw]:\n ')
            if drop_card_index in ['stop','draw']:
                if drop_card_index == 'draw' and not draw:
                    print('You cannot draw!\n') 
                    continue
                else:
                    break  
            if not drop_card_index.isdigit(): continue
            compatible = check_one(comp_cards_one,drop_card_index,stash,op)
            if compatible: # accepts if == to color and type
                x = move_card(mydeck.newdeck,player_one.player_one,player_two.player_two,drop_card_index,stash,comp_cards_one)
                if x == 1: 
                    break
                elif x == 0:
                    continue
                else:
                    op = False
                draw = False                       
            elif not compatible:
                print('Not Compatible!\n')
        if draw:
            player_one.player_one.append(mydeck.newdeck.pop())
            print('Finished Drawing One Card!\n')
            display(player_one.player_one,stash,comp_cards_one)
    
            """
            PLAYER TWO TURN HERE
            """
        op = True
        draw = True
        os.system('cls')
        while True:
            os.system('cls')


            comp_cards_two = comp_cards(player_two.player_two,stash,op)
            display(player_two.player_two,stash,comp_cards_two)
             # display mycards, and the top card
            drop_card_index = input('PLAYER 2 : What card to drop [index] or [draw]: \n')
            if drop_card_index in ['stop','draw']:
                if drop_card_index == 'draw' and not draw:
                    print('You cannot draw!\n')
                    continue
                else:
                    break
            if not drop_card_index.isdigit(): continue
            compatible = check_one(comp_cards_two,drop_card_index,stash,op)
            if compatible: # accepts if == to color and type
                x = move_card(mydeck.newdeck,player_two.player_two,player_one.player_one,drop_card_index,stash,comp_cards_two)
                if x == 1: 
                    break
                elif x == 0:
                    continue
                else:
                    op = False                        
                draw = False
            elif not compatible:
                print('Not Compatible!\n')
        if draw:
            player_two.player_two.append(mydeck.newdeck.pop())
            print('Finished Drawing One Card!\n')
            display(player_two.player_two,stash,comp_cards_two)
        

            
    
            
        ''' 
        Next Feature:"
        Function that checks the deck, and prints out only the compatible cards. 
        if len(deck) == 0:
            then automatically draws one card!
        TASK 1 : Clean up the code, try to put the functions and classes into another python file for better documentation
        TASK 2 : Find alternate solutions to using IF statements
        '''
        # we need to break this loop, either by hitting stop or by using a wildcard/draw card


print('hey')      
print('\n' * 5)