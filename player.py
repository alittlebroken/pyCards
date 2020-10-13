'''
    player.py
    A simple representation of a player class
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-13
'''
'''Class to represent a player'''
class player:

    '''Class constructor'''
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.bust = False
        self.win = False
        self.card_deck = []
        self.stick = False

    '''Add a card to the players hand'''
    def addCard(self, card):
        self.card_deck.append(card)


    '''Check the players score'''
    def checkScore(self):

        '''Always reset the score to 0 for each check'''
        self.score = 0

        '''Now loop through the hand and add the values of the cards together'''
        for x in range(len(self.card_deck)):
            self.score += self.card_deck[x].value

        '''We do not want the players score to go above 21 (bust)'''
        if self.score > 21:
            self.bust = True
            self.win = False
        elif self.score == 21:
            self.bust = False
            self.win = True
        else:
            self.bust = False
            self.win = False

    '''Show the players hand'''
    def showHand(self):

        for x in range(len(self.card_deck)):
            print("{} of {}".format(self.card_deck[x].card,self.card_deck[x].suit))