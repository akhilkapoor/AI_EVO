'''
@author: Akhil Kapoor, Michael Smith
'''

import random
from copy import deepcopy
from Player import Player
from Heuristic import Heuristic
from Direction import Direction
from GlobalParams import *

import pygame, sys
from pygame.locals import *

WHITE   = (255, 255, 255)
FPS = 30 # frames per second setting
L_GREEN = (  0, 220,   0)
N_BLUE  = (  0,   0, 128)
PURPLE  = (200,   0, 200)
RED     = (255,   0,   0)
RESIZE_FACTOR = 20

class Game(object):

    p1 = None
    p2 = None
    size = 0
    board = []
    prev_board = []
    game = 0
    D = 0
    display = False
    

    def __init__(self, player1, player2, n):
        self.p1 = player1
        self.p2 = player2
        
        self.size = n
        
        self.p1.pos = [self.size/2,self.size/4]
        self.p2.pos = [self.size/2,3*self.size/4]
        
        self.p1.direction = Direction().East
        self.p2.direction = Direction().West
        
#        self.display = True
                
        self.D = RESIZE_FACTOR

    def initialize_board(self):
        
        self.board = []
        n = self.size
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
        
        if self.display:
            pygame.init()
            fpsClock = pygame.time.Clock()
            DISPLAYSURF = pygame.display.set_mode((self.size*self.D, self.size*self.D))
            pygame.display.set_caption('Tron!')

            D = self.D

            pygame.draw.line(DISPLAYSURF, WHITE, (0, 0), (0, self.size*D), D)
            pygame.draw.line(DISPLAYSURF, WHITE, (0, 0), (self.size*D, 0), D)
            pygame.draw.line(DISPLAYSURF, WHITE, (0, self.size*D), (self.size*D, self.size*D), D)
            pygame.draw.line(DISPLAYSURF, WHITE, (self.size*D, 0), (self.size*D, self.size*D), D)

        while (not self.game):

            move1 = self.p1.pick_move(self.board, self.p2.pos)
            move2 = self.p2.pick_move(self.board, self.p1.pos)
            old_board = deepcopy(self.board)

            self.p1.prev_pos = self.p1.pos[:]
            self.p2.prev_pos = self.p2.pos[:]

            temp1 = self.p1.apply_move(move1, old_board)
            temp2 = self.p2.apply_move(move2, old_board)

            self.board = self.p1.make_move(move1, self.board)
            self.board = self.p2.make_move(move2, self.board)
            
            if self.display:
                pygame.draw.line(DISPLAYSURF, L_GREEN, (self.p1.prev_pos[1]*D, self.p1.prev_pos[0]*D), (self.p1.pos[1]*D, self.p1.pos[0]*D), D)
                pygame.draw.line(DISPLAYSURF, PURPLE, (self.p2.prev_pos[1]*D, self.p2.prev_pos[0]*D), (self.p2.pos[1]*D, self.p2.pos[0]*D), D)
                pygame.display.update()
                fpsClock.tick(FPS)
        
            #self.describe_board(self.board)

            if self.is_equal(old_board, self.board):
                # trying to step on each other's head
#                self.game = 3
                if Global().DEBUG:
                    print 'draw1'
                self.do_something()
                return None
            elif self.is_equal(temp1, temp2):
                # trying to get to the same spot
#                self.game = 3
                if Global().DEBUG:
                    print 'draw2'
                self.do_something()
                return None
            
            elif self.is_equal(temp1, old_board):
                # only p1 crashed
#                self.game = 2
                if Global().DEBUG:
                    print 'p1 crashed'
                self.do_something()
                return self.p2
            elif self.is_equal(temp2, old_board):
                # only p2 crashed
#                self.game = 1
                if Global().DEBUG:
                    print 'p2 crashed'
                self.do_something()
                return self.p1
            
            #self.describe_board(self.board)
            #self.board = final
            #c += 1
            #if c % 2 == 0:
            
        # just staying here but never executes.
        return random.choice([self.player1, self.player2, None])
    

    def do_something(self):
    
        if self.display:
            fpsClock = pygame.time.Clock()
            FPS = 120 # frames per second setting
            condition = True
        
            while condition:
                for event in pygame.event.get():
                    if event.type == KEYUP:
                        if event.key == K_SPACE:
                            condition = False
                            break
                            #pygame.quit()
                        elif event.key == K_ESCAPE:
                            sys.exit()
                    pygame.display.update()
                    fpsClock.tick(FPS)
                pygame.display.update()
                fpsClock.tick(FPS)
