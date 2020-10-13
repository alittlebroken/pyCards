#!/bin/bash/python
'''
    cards.py
    A simple electronic deck of cards
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-09
'''

'''Import shuffle'''
from random import shuffle

'''Import the card deck'''
from carddeck import suits, cards, card_values, card

'''Import the player'''
from player import player

'''Class to represent a deck of cards'''
class deck:

    '''Class constructor'''
    def __init__(self):

        '''Holds the deck of cards'''
        self.card_deck = []

        '''Generate a deck of cards'''
        for x in range(len(suits)):
            for y in range(len(cards)):
                self.card_deck.append(card(suits[x], cards[y], card_values[y]))

        '''Shuffle the deck'''
        shuffle(self.card_deck)


    '''Print out the deck of cards'''
    def showDeck(self):

        for x in range(len(self.card_deck)):
            print("{} of {}".format(self.card_deck[x].card,self.card_deck[x].suit))

    '''Deal a card from the deck'''
    def deal(self):

        return self.card_deck.pop()


'''Run the main portion of the script'''
if __name__ == '__main__':

    '''Create an instance of the card deck'''
    deck_o_cards = deck()

    player1_name = input("Player 1 please enter in your name: ")
    player1 = player(player1_name)

    dealer = player("Python Dealer Terry")

    '''Deal a hand to the player'''
    player1.addCard(deck_o_cards.deal())
    player1.addCard(deck_o_cards.deal())

    '''Deal a hand to the dealer'''
    dealer.addCard(deck_o_cards.deal())
    dealer.addCard(deck_o_cards.deal())

    print()
    print("The hand dealt to {} is:".format(player1.name))
    player1.showHand()

    game_loop = True

    while game_loop:

        print()
        '''Check the players score and display it to them'''
        player1.checkScore()
        print("You currently have {}".format(player1.score))
        print()
        print("You can do one of the following:")
        print("1. Quit")
        print("2. Hit")
        print("3. Stay")
        player1_choice = input("Enter your choice (1,2 or 3): ")

        if int(player1_choice) == 1:
            game_loop = False
        elif int(player1_choice) == 2:
            '''Give the player another card'''
            player1.addCard(deck_o_cards.deal())
        elif int(player1_choice) == 3:
            pass


        '''Check the player score and determine if we have won or not'''
        if player1.bust:
            print("Tough luck old bean. You have busted.")
            game_loop = False
        elif player1.win:
            print("Congratulations old bean. You have won.")
            game_loop = False


    print("Thank you for playing")
