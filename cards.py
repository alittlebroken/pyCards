#!/bin/bash/python
'''
    cards.py
    A simple electronic deck of cards
    Paul Lockyer (plockyer@googlemail.com)
    2020-10-09
'''

# Imports
from gameEngine import gameEngine


# Run the main portion of the script
if __name__ == '__main__':

    # Create an instance of the game engine
    game = gameEngine()

    while game.running:
        game.update()

    print("Thank you for playing")
