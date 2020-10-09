#!/bin/bash/python
'''
    cards.py
    A simple electronic deck of cards
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-09
'''

'''Import shuffle'''
from random import shuffle

'''List of  suits'''
suits = ['HEARTS','CLUBS','SPADES','DIAMONDS']

'''List of card numbers'''
cards = ['ACE',2,3,4,5,6,7,8,9,10,'JACK','QUEEN','KING']

'''Class to represent a single card in a deck'''
class card:

    '''
    The class constructor, used to setup the card
    Takes in the suit of the card and its bumber 1 to 14
    '''
    def __init__(self,suit,card):
        self.suit = suit
        self.card = card

'''Class to represent a player'''
class player:

    card_deck = []

    '''Class constructor'''
    def __init__(self,name):
        self.name = name

    '''Add a card to the players hand'''
    def addCard(self, card):
        self.card_deck.append(card)

    '''Show the players hand'''
    def showHand(self):

        for x in range(len(self.card_deck)):
            print("{} of {}".format(self.card_deck[x].card,self.card_deck[x].suit))


'''Class to represent a deck of cards'''
class deck:

    '''Class constructor'''
    def __init__(self):

        '''Holds the deck of cards'''
        self.card_deck = []

        '''Generate a deck of cards'''
        for x in range(len(suits)):
            for y in range(len(cards)):
                self.card_deck.append(card(suits[x],cards[y]))

        '''Shuffle the deck'''
        shuffle(self.card_deck)


    '''Print out the deck of cards'''
    def showDeck(self):

        for x in range(len(self.card_deck)):
            print("{} of {}".format(self.card_deck[x].card,self.card_deck[x].suit))

    '''Deal X number of cards'''
    def deal(self):

        return self.card_deck.pop()


'''Run the main portion of the script'''
if __name__ == '__main__':

    '''Create an instance of the card deck'''
    deck_o_cards = deck()

    '''Show the currently shuffled deck'''
    deck_o_cards.showDeck()

    player1_name = input("Player 1 please enter in your name: ")
    player1 = player(player1_name)

    '''Deal a hand to the player'''
    player1.addCard(deck_o_cards.deal())
    player1.addCard(deck_o_cards.deal())
    player1.addCard(deck_o_cards.deal())
    player1.addCard(deck_o_cards.deal())
    player1.addCard(deck_o_cards.deal())

    print()
    print("The hand dealt to {} is:".format(player1.name))
    print()
    player1.showHand()
