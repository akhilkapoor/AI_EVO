'''
Created on Sep 6, 2012

@author: Mike
'''

import random

class Game(object):
    '''
    classdocs
    '''
    player1 = None
    player2 = None

    def __init__(self, player1, player2):
        '''
        Constructor
        '''
        self.player1 = player1
        self.player2 = player2
        
    def play(self):
        
        # play game between player1 and player2

        # should return the winning player (random for now)
        # returns None if 'draw'
        
        return random.choice([self.player1, self.player2, None])