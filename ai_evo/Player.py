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
        self.direction = Direction()
        #prev_pos = [0,0]
        

    def applicable_moves(self, board):
        moves = direction.get_others()
        return moves
    
    def apply_move(self, move, old_board):
        posx = self.position[0] + move[0]
        posy = self.position[1] + move[1]
        new_board = deepcopy(old_board)
        new_board[posx][posy] = 1
        return new_board

    def pick_move(self, board, op_pos):
        moves = self.applicable_moves(board)
        scores = []
        for m in moves:
            new_board = apply_move(m, board)
            score.append(self.heuristic.eval(board, new_board, self.pos, op_pos))
        best_move = moves[ scores.index( max(scores) ) ]
        return best_move

    def describe_move(self, move):
        print move

    def user_move(self):
        # input from somewhere
        return 'direction'
