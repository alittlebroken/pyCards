#!/bin/bash/python
'''
    cards.py
    A simple electronic deck of cards
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-09
'''

# Imports
from random import randint
from carddeck import suits, cards, card_values, card, deck
from player import player

# Run the main portion of the script
if __name__ == '__main__':

    # Create an instance of the card deck
    deck_o_cards = deck()

    player1 = player("Player Bot#{}".format(randint(0,100000)))

    dealer_bot = player("Dealer Bot#{}".format(randint(0,100000)))

    # Deal a hand to the player
    player1.addCard(deck_o_cards.deal())
    player1.addCard(deck_o_cards.deal())

    # Deal a hand to the dealer
    dealer_bot.addCard(deck_o_cards.deal())
    dealer_bot.addCard(deck_o_cards.deal())

    print()
    print("The hand dealt to {} is:".format(player1.name))
    player1.showHand()

    game_loop = True

    while game_loop:

        # Check if the player already has 21 before we begin or the dealer
        player1.checkScore()
        dealer_bot.checkScore()
        if player1.win and not dealer_bot.win:
            print()
            print("#" * (len("WINNER!") + 4))
            print("# WINNER! #")
            print("#" * (len("WINNER!") + 4))
            print()
            game_loop = False
        elif player1.stick and dealer_bot.stick:
            # Both dealer and player have stuck, lets see who won
            if player1.score > dealer_bot.score:
                print()
                print("#" * (len("WINNER!") + 4))
                print("# WINNER! #")
                print("#" * (len("WINNER!") + 4))
                game_loop = False
                print()
            elif player1.score <= dealer_bot.score:
                print()
                print("#" * (len("LOSER!") + 4))
                print("# LOSER! #")
                print("#" * (len("LOSER!") + 4))
                print()
                game_loop = False
        elif player1.win and dealer_bot.win:
            print()
            if player1.score > dealer_bot.score:
                print("#" * (len("WINNER!") + 4))
                print("# WINNER! #")
                print("#" * (len("WINNER!") + 4))
                game_loop = False
            elif player1.score < dealer_bot.score:
                print()
                print("#" * (len("LOSER!") + 4))
                print("# LOSER! #")
                print("#" * (len("LOSER!") + 4))
                print()
                game_loop = False
            elif player1.score == dealer_bot.score:
                print()
                print("#" * (len("LOSER!") + 4))
                print("# LOSER! #")
                print("#" * (len("LOSER!") + 4))
                print()
                game_loop = False
            print()
        elif player1.bust:
            print()
            print()
            print("#" * (len("LOSER!")) + 4)
            print("# LOSER! #")
            print("#" * (len("LOSER!")) + 4)
            print()
            print()
            game_loop = False
        elif dealer_bot.bust:
            print()
            print("#" * (len("WINNER!")) + 4)
            print("# WINNER! #")
            print("#" * (len("WINNER!")) + 4)
            game_loop = False
            print()
        else:

            # Only ask for further options from the player if they have not already stuck
            if not player1.stick:
                print()
                print("You currently have {}".format(player1.score))
                print("The dealer has {}".format(dealer_bot.score))
                print()
                print("You can do one of the following:")
                print("1. Quit")
                print("2. Hit")
                print("3. Stick")
                print()
                player1_choice = input("Enter your choice (1,2 or 3): ")

                if int(player1_choice) == 1:
                    game_loop = False
                elif int(player1_choice) == 2:
                    # Give the player another card
                    player1.addCard(deck_o_cards.deal())
                    player1.checkScore()
                    print()
                    print("Players hand:")
                    print()
                    player1.showHand()
                elif int(player1_choice) == 3:
                    player1.stick = True

            # Process the dealer actions here
            print()
            print("Processing {} actions".format(dealer_bot.name))
            print()

            # Determine if we need to deal another card to the dealer
            # But only if they have not already stuck
            if not dealer_bot.stick:
                if (21 - dealer_bot.score) >= 16:
                    # Deal a new card and take a risk
                    dealer_bot.addCard(deck_o_cards.deal())
                    dealer_bot.checkScore()
                    print("{} new score is {}".format(dealer_bot.name, dealer_bot.score))
                else:
                    # Do nothing
                    dealer_bot.stick = True
                    dealer_bot.checkScore()
                    print("{} has passed this turn".format(dealer_bot.name))

    print("Thank you for playing")
