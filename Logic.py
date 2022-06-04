
import os
import random
from Classes import Deck,Cards,Player
import Classes

game = True


while game: # Initializes the game

    mydeck = Deck() # Creates the deck
    random.shuffle(mydeck.newdeck) # Shuffles the deck
    player_one = Player() 
    player_two = Player()
    stash = [] 

    for _ in range(7):

        player_one.player_one.append(mydeck.deal_one())
        player_two.player_two.append(mydeck.deal_one())
    
    x,y = random.choice(Deck.colors[1:]),random.choice(Deck.card_type[:11]) # Creates a random top card (no wildcards and action cards)
    first_card = Classes.Cards(x,y)

    stash.append(first_card) #adds to the stash, becomes the top card

    while True: 

        if len(player_one.player_one) == 0: # Breaks the loop if any of the player's card is == 0
            print('PLAYER ONE HAS WON THE GAME!')
            break

        elif len(player_two.player_two) == 0:
            print('PLAYER TWO HAS WON THE GAME!')
            break

        else:
            
            op = True # Bool for determining whether color == color is compatible

            draw = True # Bool for determining whether a player should draw if player
                        # did not drop a single card 

            while True: 
                
                os.system('cls') # Clears the terminal

                comp_cards_one = Classes.comp_cards(player_one.player_one,stash,op) # Compatible cards in player's deck

                Classes.display(player_one.player_one,stash,comp_cards_one) # Displays top card, player's cards, compatible cards

                drop_card_index = input('PLAYER 1 : What card to drop? [index] [draw] [stop]:\n ') # User prompt

                if drop_card_index == 'end': # End the program
                    2 + '3'

                if drop_card_index[0].lower() in ['s','d']: 
                    if drop_card_index == 'draw' and not draw: # If player chooses to draw, and he has already dropped a card
                                                               # it continues the loop
                        print('You cannot draw!\n') 
                        continue
                    else: # If player hasn't dropped a card and chooses to draw, it breaks the loop (player 2's turn)
                        break  

                if not drop_card_index.isdigit(): continue # Checks if the input is a digit, else it restarts the prompt

                compatible = Classes.check_one(comp_cards_one,drop_card_index,stash,op) # It checks if the card chosen is compatible

                if compatible: 

                    x = Classes.move_card(mydeck.newdeck,player_one.player_one,\
                    player_two.player_two,drop_card_index,stash,comp_cards_one) # Initalizes the card

                    if x == 1: # If it returns 1, it finishes player one's turn
                        draw = False # Cannot draw
                        break

                    elif x == 0: # (skip,reverse) Continues player's turn
                        continue
                    else:
                        op = False # It means a card has been drop, which only allows == card type
                                   # on the next card drop

                    draw = False   # Cannot draw since a card has already been dropped

                elif not compatible: # Continues the loop!
                    print('Not Compatible!\n')

            if draw: # If bool draw is true, draws one card

                player_one.player_one.append(mydeck.newdeck.pop())
                print('Finished Drawing One Card!\n')
                Classes.display(player_one.player_one,stash,comp_cards_one)

                """
                PLAYER TWO TURN HERE:
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

    while again_prompt[0].lower() not in ['y','n']: # Play again prompt
        again_prompt = input('Would you like to play again? [Yes/No]: \n')

    if again_prompt[0] == 'y':
        continue
    else:
        game = False

           
print('GAME OVER! Thank you for playing!')
# GAME OVER


