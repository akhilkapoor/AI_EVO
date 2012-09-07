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

    def __init__(self, pos):
        #self.name = name
        self.position = pos[:]
        self.direction = Direction()

    def applicable_moves(self, board):
        moves = direction.get_others()
        return moves
    
    def apply_move(self, move, old_board):
        self.position[0] += move[0]
        self.position[1] += move[1]
        new_board = deepcopy(old_board)
        new_board[self.pos[0]][self.pos[1]] = self.color
        return new_board

    def describe_move(move):
        print move

    def apply_heuristic(self, board):
        return self.heuristic(board)

    def set_heuristic(self, H):
        self.heuristic = H

    def user_move(self):
        # input from somewhere
        return 'direction'
