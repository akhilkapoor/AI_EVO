'''
@author: Michael Smith, Akhil Kapoor
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
        pass
        
    def get_others(self, direction):
        others = deepcopy(self.all)
        others.remove(direction)
        return others
        
    def __str__(self, direction):
        if direction == self.North:
            return 'North'
        elif direction == self.East:
            return "East"
        elif direction == self.South:
            return "South"
        elif direction == self.West:
            return "West"
