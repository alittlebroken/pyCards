'''
    carddeck.py
    A simple representation of a card deck in python
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-13
'''
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