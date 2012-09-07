'''
@author: Akhil Kapoor, Michael Smith
'''
    
#import random
from copy import deepcopy
from Player import Player
from Heuristic import Heuristic

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
        self.board = []
        for i in range(n):
            self.board.append([0]*n)
        for i in range(n):
            self.board[0][i] = 1
            self.board[n-1][i] = 1
            self.board[i][0] = 1
            self.board[i][n-1] = 1
        p1pos = self.p1.pos
        p2pos = self.p2.pos
        self.board[p1pos[0]][p1pos[1]] = 1
        self.board[p2pos[0]][p2pos[1]] = 1

    # Any collision - head-on, next-move, tail, wall
    def is_equal(self, board1, board2):
        if board1 == board2:
            return True
        else:
            return False

    def describe_board(self, board):
        print
        print '   ',
        for i in range(self.size):
            print i,
        print
        print '- -',
        for i in range(self.size):
            print '-',
        print
        for i in range(self.size):
            print i, '|', 
            for j in range(self.size):
                print board[i][j],
            print
        print
        
    def play(self):
        c = 0
        while (not self.game):

            move1 = self.p1.pick_move(self.board, self.p2.pos)
            move2 = self.p2.pick_move(self.board, self.p1.pos)
            old_board = deepcopy(self.board)

            temp1 = self.p1.apply_move(move1, old_board)
            temp2 = self.p2.apply_move(move2, old_board)

            self.board = self.p1.make_move(move1, self.board)
            self.board = self.p2.make_move(move2, self.board)

            self.describe_board(self.board)

            if self.is_equal(old_board, self.board):
                # trying to step on each other's head
#                self.game = 3
                print 'draw1'
                return None
            elif self.is_equal(temp1, temp2):
                # trying to get to the same spot
#                self.game = 3
                print 'draw2'
                return None
            elif self.is_equal(temp1, old_board):
                # only p1 crashed
#                self.game = 2
                print 'p1 crashed'
                return self.p2
            elif self.is_equal(temp2, old_board):
                # only p2 crashed
#                self.game = 1
                print 'p2 crashed'
                return self.p1


            #self.describe_board(self.board)
#            self.board = final
            c += 1
#            if c % 2 == 0:
            
        # just staying here but never executes.
        return random.choice([self.player1, self.player2, None])
    
