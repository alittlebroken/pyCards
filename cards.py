#!/bin/bash/python
'''
    cards.py
    A simple electronic deck of cards
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-09
'''

# Imports
from random import randint
from carddeck import deck
from player import player

# Display an important message on screen ( I.E you have won )
def displayImportantMessage(message):
    print()
    print("*" * (len(message) + 4))
    print("* {} *".format(message))
    print("*" * (len(message) + 4))
    print()


class gameEngine:
    '''A very simple engine for the card game 21 (BlackJack)'''

    # Class constructor
    def __init__(self):
        self.title = "PyCard - A simple game of 21 ( Blackjack )"
        self.running = True
        self.dealer = player("Dealer Bot#{}".format(randint(0,100000)))
        self.player = player("Player Bot#{}".format(randint(0, 100000)))
        self.card_deck = deck()

        # Deal out the initial two cards to the dealer and player
        self.dealer.addCard(self.card_deck.deal())
        self.dealer.addCard(self.card_deck.deal())

        self.player.addCard(self.card_deck.deal())
        self.player.addCard(self.card_deck.deal())

    # Draw the menu of the game
    def displayMenu(self):
        print()
        print("*" * (len(self.title) + 4))
        print("* {} *".format(self.title))
        print("*" * (len(self.title) + 4))
        print()
        print("1. Quit")
        print("2. Hit")
        print("3. Stick - No more actions this game")
        self.displayScores()

    # Display player and dealer scores
    def displayScores(self):
        print()
        print("Dealers Score: {}".format(self.dealer.score))
        print("Players Score: {}".format(self.player.score))
        print()

    def displayResult(self, message):
        print()
        print("*" * (len(message) + 4))
        print("* {} *".format(message))
        print("*" * (len(message) + 4))

    # Display the last card added to a hand
    def displayLastCard(self, person):
        print("{} was dealt {} of {}".format(person.name, person.card_deck[-1].card, person.card_deck[-1].suit))
        print("Their score is now {}".format(person.score))

    # Update the game
    def update(self):

        # Process player input only if the player has not stuck
        if not self.player.stick:

            self.player.checkScore()
            self.dealer.checkScore()

            self.displayMenu()
            player_choice = int(input("Please choose an option (1,2, or 3): "))

            print()

            if player_choice == 1:
                # Quit the game
                self.running = False
                print("{} has decided to quit the game".format(self.player.name))
            elif player_choice == 2:
                # Deal a new card
                self.player.addCard(self.card_deck.deal())
                self.player.checkScore()
                print("{} has decided to hit".format(self.player.name))
                self.displayLastCard(self.player)
            elif player_choice == 3:
                # The player has decided to stick with the cards he has
                self.player.stick = True
                self.player.checkScore()
                print("{} has decided to stick".format(self.player.name))

        # Process dealer input only if the dealer has not stuck
        if not self.dealer.stick:
            # Will the dealer draw a card?
            if (21 - self.dealer.score) >= 15:
                self.dealer.addCard(self.card_deck.deal())
                self.dealer.checkScore()
                print("{} has decided to hit".format(self.dealer.name))
                self.displayLastCard(self.dealer)
            else:
                # Dealer will stick
                self.dealer.stick = True
                self.player.checkScore()
                print("{} has decided to stick".format(self.dealer.name))

        # Check player/dealer flags against game rules

        if self.player.win and self.dealer.win:
            # House always wins
            self.displayResult("House wins")
            self.running = False
        elif self.player.win and not self.dealer.win:
            # Player wins
            self.displayResult("Player wins")
            self.running = False
        elif self.player.bust:
            # Player loses
            self.displayResult("Player busts")
            self.running = False
        elif self.dealer.bust:
            # Player wins - dealer busted
            self.displayResult("Player wins - dealer busted")
            self.running = False
        elif self.player.stick and self.dealer.stick:
            # Both parties have stuck lets see who wins based on score
            if self.player.score > self.dealer.score:
                self.displayResult("Player wins")
                self.running = False
            elif self.player.score == self.dealer.score:
                self.displayResult("House wins")
                self.running = False
            elif self.player.score <= self.dealer.score:
                self.displayResult("House wins")
                self.running = False


# Run the main portion of the script
if __name__ == '__main__':

    # Create an instance of the game engine
    game = gameEngine()

    while game.running:
        game.update()

    print("Thank you for playing")
