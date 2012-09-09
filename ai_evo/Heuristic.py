'''
@author: Michael Smith, Akhil Kapoor
'''

import random
import math
from GlobalParams import *

class Heuristic(object):
    weights = []

    def __init__(self):
        '''
        Constructor
        '''
        
    def eval(self, old_board, new_board, p1_pos, p2_pos):
        
        score = 0
        
        score -= self.weights[0] * self.i_crash(old_board, new_board)
        score += self.weights[1] * self.opp_proximity(p1_pos, p2_pos)

        return score
    
    def region_difference(self):
        # p1 region - p2 region
        
        pass
    
    def i_crash(self, old_board, new_board):
        return old_board == new_board
    
    # distance from my opponent
    def opp_proximity(self, p1_pos, p2_pos):
        return math.sqrt( (p1_pos[0]-p2_pos[0])**2 + (p1_pos[0]-p2_pos[0])**2 )
    
    