'''
@author: Michael Smith, Akhil Kapoor
'''

import random
import math
from Direction import Direction
from GlobalParams import *
from copy import deepcopy

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
        score += self.weights[2] * self.region_difference(old_board, p1_pos, p2_pos)

        return score
    
    def region_difference(self, old_board, p1_pos, p2_pos):
        return self.flood_fill(old_board, p1_pos) - self.flood_fill(old_board, p2_pos)
    
    def i_crash(self, old_board, new_board):
        return old_board == new_board
    
    # distance from my opponent
    def opp_proximity(self, p1_pos, p2_pos):
        return math.sqrt( (p1_pos[0]-p2_pos[0])**2 + (p1_pos[0]-p2_pos[0])**2 )
    
    # flood fill algorithm (see wikipedia)
    
    def flood_fill(self, board, pos):
        d = Direction()
        spaces_filled = 0
        empty = 0
        filled = 1
        b = deepcopy(board)
        q = [pos]               # 2. Add node to the end of Q.
        while len(q) > 0:       # 4. While Q is not empty: 
            n = q.pop()         # 5. Set n equal to the last element of Q, and remove last element from Q     
            if b[n[0]][n[1]] == empty:   # 8. If the color of n is equal to target-color:
                b[n[0]][n[1]] = filled   # 9. Set the color of n to replacement-color.
                spaces_filled += 1
                q.append(d.get_new_coord(n, Direction.North)) # 10. Add North node to end of Q.
                q.append(d.get_new_coord(n, Direction.East))  # 11. Add East node to end of Q.
                q.append(d.get_new_coord(n, Direction.South))  # 12. Add South node to end of Q.
                q.append(d.get_new_coord(n, Direction.West))   # 13. Add West node to end of Q.
                
        return spaces_filled    # 14. Return.