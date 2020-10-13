#!/bin/bash/python
'''
    cards.py
    A simple electronic deck of cards
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-09
'''

# Import shuffle
from random import shuffle

# Import the card deck
from carddeck import suits, cards, card_values, card

# Import the player
from player import player

# Class to represent a deck of cards
class deck:

    # Class constructor
    def __init__(self):

        # Holds the deck of cards
        self.card_deck = []

        # Generate a deck of cards
        for x in range(len(suits)):
            for y in range(len(cards)):
                self.card_deck.append(card(suits[x], cards[y], card_values[y]))

        # Shuffle the deck
        shuffle(self.card_deck)


    # Print out the deck of cards
    def showDeck(self):

        for x in range(len(self.card_deck)):
            print("{} of {}".format(self.card_deck[x].card,self.card_deck[x].suit))

    # Deal a card from the deck
    def deal(self):

        return self.card_deck.pop()


# Run the main portion of the script
if __name__ == '__main__':

    # Create an instance of the card deck
    deck_o_cards = deck()

    player1_name = input("Player 1 please enter in your name: ")
    player1 = player(player1_name)

    dealer_bot = player("Computer")

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
            print("Wow! Congratulations you have won.")
            print()
            game_loop = False
        if player1.win and dealer_bot.win:
            print()
            if player1.score > dealer_bot.score:
                print("Wow! Congratulations you have won.")
                game_loop = False
            elif player1.score < dealer_bot.score:
                print("Such a shame. Perhaps you will have better luck next time.")
                game_loop = False
            elif player1.score == dealer_bot.score:
                print("Such a shame. House always wins. Better luck next play.")
                game_loop = False
            print()
        elif player1.bust:
            print()
            print("Such a shame. Perhaps you will have better luck next time.")
            print()
            game_loop = False
        elif dealer_bot.bust:
            print()
            print("The dealer has bust. Congratulations you win.")
            game_loop = False
            print()
        else:
            print()
            print("You currently have {}".format(player1.score))
            print("The dealer has {}".format(dealer_bot.score))
            print()
            print("You can do one of the following:")
            print("1. Quit")
            print("2. Hit")
            print("3. Stay")
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
                pass

            # Process the dealer actions here


    print("Thank you for playing")
