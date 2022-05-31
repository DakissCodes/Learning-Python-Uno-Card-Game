import os


import random
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from xml.dom.expatbuilder import FragmentBuilderNS
from Classes import Deck,Cards,Player



def move_card(alldeck,deck,deck2,index,stash):
    index = int(index) - 1
    card = deck[index]
    if card.card_type == 'Skip' or card.card_type == 'Reverse':
        print('Your turn again!')
        stash.append(deck.pop(int(index))) # CHANGE THIS: WE CAN USE deck,index(card)
        return 0

    elif card.card_type == 'DrawTwo':
        for _ in range(2): deck2.append(alldeck.pop())
        print('Player 2 has drawn 2 cards!\n')
        stash.append(deck.pop(int(index)))
        return 1

    elif card.card_type == 'WildDrawFour':
        for _ in range(4): deck2.append(alldeck.pop())
        print('Player 2 has drawn 4 cards!\n')
        change_color = ''
        while change_color.lower() not in ['green','red','blue','yellow']:
            change_color = input('What color would you like to change to? :\n ')
        card.color = change_color.capitalize()
        stash.append(deck.pop(int(index)))
        return 1

    elif card.card_type == 'Wild':
        change_color = ''
        while change_color.lower() not in ['green','red','blue','yellow']:
            change_color = input('What color would you like to change to? :\n ')
        card.color = change_color.capitalize()   
        stash.append(deck.pop(int(index)))
        return 1
    
    else:
        stash.append(deck.pop(int(index)))


def display(deck,stash_deck):
    print(f'THE TOP CARD: {stash_deck[-1]}\n')
    print('\n')
    print('YOUR CARDS: ' +  ' , '.join([str(_) for _ in deck]))
def check_one(player_one_deck,index,stash_deck,op):
    index = int(index) - 1
    card = player_one_deck[int(index)]
    face_card = stash_deck[-1]
    if op:
        if card.color == 'All': 
            return True
        elif card.color == face_card.color:
            return True
        elif card.card_type == face_card.card_type:
            return True
        else:
            return False
    elif not op:
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
        comp_cards = [_ for _ in deck1 if _.card_type == top_card.card_type or _.color == 'All']
    return 'USE: ' + ' , '.join([str(_) for _ in comp_cards])



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



            display(player_one.player_one,stash) # display mycards, and the top card
            print(comp_cards(player_one.player_one,stash,op))
            drop_card_index = input('PLAYER 1 : What card to drop? [index] or [draw]:\n ')
            if drop_card_index in ['stop','draw']:
                if drop_card_index == 'draw' and not draw:
                    print('You cannot draw!\n') 
                    continue
                else:
                    break  
            compatible = check_one(player_one.player_one,drop_card_index,stash,op)
            if compatible: # accepts if == to color and type
                x = move_card(mydeck.newdeck,player_one.player_one,player_two.player_two,drop_card_index,stash)
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
            display(player_one.player_one,stash)
    
            """
            PLAYER TWO TURN HERE
            """
        op = True
        draw = True
        os.system('cls')
        while True:
            os.system('cls')



            display(player_two.player_two,stash) # display mycards, and the top card
            drop_card_index = input('PLAYER 2 : What card to drop [index] or [draw]: \n')
            if drop_card_index in ['stop','draw']:
                if drop_card_index == 'draw' and not draw:
                    print('You cannot draw!\n')
                    continue
                else:
                    break
            compatible = check_one(player_two.player_two,drop_card_index,stash,op)
            if compatible: # accepts if == to color and type
                x = move_card(mydeck.newdeck,player_two.player_two,player_one.player_one,drop_card_index,stash)
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
            display(player_two.player_two,stash)
        

            
    
            
        ''' 
        Next Feature:"
        Function that checks the deck, and prints out only the compatible cards. 
        if len(deck) == 0:
            then automatically draws one card!
        '''
        # we need to break this loop, either by hitting stop or by using a wildcard/draw card


print('hey')      
print('\n' * 5)