'''
Created on Sep 6, 2012

@author: Mike
'''
from copy import deepcopy

class Direction(object):
    North = [0,-1]
    East = [1,0]
    South = [0,1]
    West = [-1,0]
    all = [North,East,South,West]

    def __init__(self):
        '''
        Constructor
        '''
        self.all = deepcopy(self.all)
        
    def get_others(self, direction):
        pass

        
    def __str__(self, direction):
        if direction == self.North:
            return 'North'
        elif direction == self.East:
            return "East"
        elif direction == self.South:
            return "South"
        elif direction == self.West:
            return "West"
