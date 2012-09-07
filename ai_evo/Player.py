'''
@author: Akhil Kapoor, Michael Smith
'''

from copy import deepcopy
from Direction import Direction

#   Player {
#       position : [x, y]
#       direction : north, south, east, west  // decide next or current
#       color : Blue/Pink
#       moves_made : absolute  // computer can have straight, human cannot
#       previos_position : [x, y]
#       heuristic: the heuristic function
#       }

class Player(object):

    name = None
    pos = [0, 0]
    direction = None
    color = 'B'
    prev_pos = []
    heuristic = None
    moves_made = []

    def __init__(self):
        name = None
        self.direction = Direction().North
        #prev_pos = [0,0]
        

    def applicable_moves(self, board):
        opp_direction = Direction().opposite_direction(self.direction)
        moves = Direction().get_others(opp_direction)
        return moves
    
    def apply_move(self, move, old_board):
        posx = self.pos[0] + move[0]
        posy = self.pos[1] + move[1]
        new_board = deepcopy(old_board)
        new_board[posx][posy] = 1
        return new_board

    def make_move(self, move, old_board):
        self.pos[0] += move[0]
        self.pos[1] += move[1]
        self.direction = deepcopy(move)
        new_board = deepcopy(old_board)
        new_board[self.pos[0]][self.pos[1]] = 1
        #print self.name, 'moved', Direction().__str__(move), 'to', self.pos
#        self.describe_move(best_move)
        return new_board

    def pick_move(self, board, op_pos):
        moves = self.applicable_moves(board)
        scores = []
        for m in moves:
            new_board = self.apply_move(m, board)
            newp = [self.pos[0]+m[0], self.pos[1]+m[1]]
            scores.append(self.heuristic.eval(board, new_board, newp, op_pos))
            
        best_move = moves[ scores.index( max(scores) ) ]
        print 'Scores', scores
        print 'Move', Direction().__str__(best_move)
        return best_move

    def describe_move(self, move):
        print move

    def user_move(self):
        # input from somewhere
        return 'direction'
