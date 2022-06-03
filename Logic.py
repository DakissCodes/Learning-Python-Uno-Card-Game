
import os
import random
from Classes import Deck,Cards,Player
import Classes


game = True

while game: 

    mydeck = Deck()
    random.shuffle(mydeck.newdeck)
    player_one = Player()
    player_two = Player()
    stash = []

    for _ in range(2):

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

                comp_cards_one = Classes.comp_cards(player_one.player_one,stash,op)
                Classes.display(player_one.player_one,stash,comp_cards_one) # display mycards, and the top card
                drop_card_index = input('PLAYER 1 : What card to drop? [index] or [draw]:\n ')

                if drop_card_index == 'end':
                    2 + '3'

                if drop_card_index[0].lower() in ['s','d']:
                    if drop_card_index == 'draw' and not draw:
                        print('You cannot draw!\n') 
                        continue
                    else:
                        break  

                if not drop_card_index.isdigit(): continue

                compatible = Classes.check_one(comp_cards_one,drop_card_index,stash,op)

                if compatible: # accepts if == to color and type
                    x = Classes.move_card(mydeck.newdeck,player_one.player_one,player_two.player_two,drop_card_index,stash,comp_cards_one)

                    if x == 1: 
                        draw = False  
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
                Classes.display(player_one.player_one,stash,comp_cards_one)

                """
                PLAYER TWO TURN HERE
                """
        if len(player_one.player_one) == 0:
            print('PLAYER ONE HAS WON THE GAME!')
            break

        elif len(player_two.player_two) == 0:
            print('PLAYER TWO HAS WON THE GAME!')
            break

        else:

            op = True
            draw = True
            os.system('cls')
            while True:

                os.system('cls')

                comp_cards_two = Classes.comp_cards(player_two.player_two,stash,op)
                Classes.display(player_two.player_two,stash,comp_cards_two)
                # display mycards, and the top card
                drop_card_index = input('PLAYER 2 : What card to drop [index] or [draw]: \n')

                if drop_card_index[0].lower() in ['s','d']:
                    if drop_card_index == 'draw' and not draw:
                        print('You cannot draw!\n')
                        continue
                    else:
                        break

                if not drop_card_index.isdigit(): continue
                compatible = Classes.check_one(comp_cards_two,drop_card_index,stash,op)

                if compatible: # accepts if == to color and type
                    x = Classes.move_card(mydeck.newdeck,player_two.player_two,player_one.player_one,drop_card_index,stash,comp_cards_two)
                    if x == 1: 
                        draw = False  
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
                Classes.display(player_two.player_two,stash,comp_cards_two)


    again_prompt = 'FILL'

    while again_prompt[0].lower() not in ['y','n']:
        again_prompt = input('Would you like to play again? [Yes/No]: \n')

    if again_prompt[0] == 'y':
        continue
    else:
        game = False

           
    
            
        ''' 
        TASK 1 : Clean up the code, try to put the functions and classes into another python file for better documentation
        TASK 2 : Find alternate solutions to using IF statements
        BUG: When dropping All Wild, player still draws a card!
        '''
        # we need to break this loop, either by hitting stop or by using a wildcard/draw card

print('GAME OVER! Thank you for playing!')
# GAME OVER