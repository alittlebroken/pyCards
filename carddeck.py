'''
    carddeck.py
    A simple representation of a card deck in python
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-13
'''

# Imports
from random import shuffle

'''List of  suits'''
suits = ['HEARTS','CLUBS','SPADES','DIAMONDS']

'''List of card numbers'''
cards = ['ACE',2,3,4,5,6,7,8,9,10,'JACK','QUEEN','KING']

'''Values of the cards'''
card_values = [1,2,3,4,5,6,7,8,9,10,10,10,10]

'''Class to represent a single card in a deck'''
class card:

    '''
    The class constructor, used to setup the card
    Takes in the suit of the card and its bumber 1 to 14
    '''
    def __init__(self,suit, card, value):
        self.suit = suit
        self.card = card
        self.value = value

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
