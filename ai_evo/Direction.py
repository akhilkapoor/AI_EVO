'''
@author: Michael Smith, Akhil Kapoor
'''

from copy import deepcopy
from GlobalParams import *

class Direction(object):
    North = [-1,0]
    East = [0,1]
    South = [1,0]
    West = [0,-1]
    all = [North,East,South,West]

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def get_new_coord(self, old_coord, direction):
        return [old_coord[0] + direction[0], old_coord[1] + direction[1]]
        
    def get_others(self, direction):
        others = deepcopy(self.all)
        others.remove(direction)
        return others

    def opposite_direction(self, old_d):
        new_d = [old_d[0]*-1, old_d[1]*-1]
        return new_d        
        
    def __str__(self, direction):
        if direction == self.North:
            return 'North'
        elif direction == self.East:
            return "East"
        elif direction == self.South:
            return "South"
        elif direction == self.West:
            return "West"
