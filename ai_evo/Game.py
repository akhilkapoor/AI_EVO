'''
@author: Akhil Kapoor, Michael Smith
'''
    
#import random
from Player import Player

class Game(object):

    p1 = None
    p2 = None
    size = 0
    board = []
    prev_board = []
    game = 0
    
    def __init__(self, player1, player2, s):
        self.p1 = player1
        self.p2 = player2

    def initialize_board(self, n):
        self.size = n
        for i in range(n):
            self.board.append([0]*n)
        for i in range(n):
            self.board[0][i] = 1
            self.board[n-1][i] = 1
            self.board[i][0] = 1
            self.board[i][n-1] = 1

    # Any collision - head-on, next-move, tail, wall
    def is_equal(self, board1, board2):
        if board1 == board2:
            return True
        else:
            return False

    def describe_board(self, board):
        for i in range(self.size):
            for j in range(self.size):
                print board[i][j],
            print
        print
        print
    def play(self):

        while (not self.game):

            move1 = self.p1.pick_move(board, self.p2.pos)
            move2 = self.p2.pick_move(board, self.p1.pos)
            temp1 = self.p1.apply_move(move1, board)
            temp2 = self.p2.apply_move(move2, board)
            final = self.p2.apply_move(move2, temp1)

            if is_equal(final, board):
                # trying to step on each other's head
#                self.game = 3
                return None
            elif is_equal(temp1, temp2):
                # trying to get to the same spot
#                self.game = 3
                return None
            elif is_equal(temp1, board):
                # only p1 crashed
#                self.game = 2
                return self.p2
            elif is_equal(temp2, board):
                # only p2 crashed
#                self.game = 1
                return self.p1

            board = final
            
        # just staying here but never executes.
        return random.choice([self.player1, self.player2, None])

def test():
    p1 = Player([1,1])
    p2 = Player([2,2])
    g = Game(p1, p2, 10)
    g.initialize_board(10)
    g.describe_board(g.board)
