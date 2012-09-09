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

class Game(object):

    p1 = None
    p2 = None
    board = []
    prev_board = []
    game = 0
    
    display = DISPLAY
    board_size = BOARD_SIZE

    def __init__(self, player1, player2, n):
        self.p1 = player1
        self.p2 = player2
        
        self.board_size = n
        
        self.p1.pos = [self.board_size/2,self.board_size/4]
        self.p2.pos = [self.board_size/2,3*self.board_size/4]
        
        self.p1.direction = Direction().East
        self.p2.direction = Direction().West

    def initialize_board(self):
        self.board = []
        n = self.board_size
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
        for i in range(self.board_size):
            print i,
        print
        print '- -',
        for i in range(self.board_size):
            print '-',
        print
        for i in range(self.board_size):
            print i, '|', 
            for j in range(self.board_size):
                print board[i][j],
            print
        print
        
    def play(self):       
        
        if self.display:
            pygame.init()

            F = WINDOW_SIZE/self.board_size
            
            fpsClock = pygame.time.Clock()
            
            DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption('Tron!')

            pygame.draw.line(DISPLAYSURF, WHITE, (0, 0), (0, WINDOW_SIZE), F)
            pygame.draw.line(DISPLAYSURF, WHITE, (0, 0), (WINDOW_SIZE, 0), F)
            pygame.draw.line(DISPLAYSURF, WHITE, (0, WINDOW_SIZE), (WINDOW_SIZE, WINDOW_SIZE), F)
            pygame.draw.line(DISPLAYSURF, WHITE, (WINDOW_SIZE, 0), (WINDOW_SIZE, WINDOW_SIZE), F)
            
            pygame.event.pump()

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
                pygame.draw.line(DISPLAYSURF, L_GREEN, (self.p1.prev_pos[1]*F, self.p1.prev_pos[0]*F), (self.p1.pos[1]*F, self.p1.pos[0]*F), F)
                pygame.draw.line(DISPLAYSURF, PURPLE, (self.p2.prev_pos[1]*F, self.p2.prev_pos[0]*F), (self.p2.pos[1]*F, self.p2.pos[0]*F), F)
                pygame.display.update()
                self.pygame_event_handler()
                fpsClock.tick(FPS)
        
            #self.describe_board(self.board)

            if self.is_equal(old_board, self.board):
                # trying to step on each other's head
#                self.game = 3
                if DEBUG:
                    print 'draw1'
                self.pygame_event_handler()
                return None
            elif self.is_equal(temp1, temp2):
                # trying to get to the same spot
#                self.game = 3
                if DEBUG:
                    print 'draw2'
                self.pygame_event_handler()
                return None
            
            elif self.is_equal(temp1, old_board):
                # only p1 crashed
#                self.game = 2
                if DEBUG:
                    print 'p1 crashed'
                self.pygame_event_handler()
                return self.p2
            elif self.is_equal(temp2, old_board):
                # only p2 crashed
#                self.game = 1
                if DEBUG:
                    print 'p2 crashed'
                self.pygame_event_handler()
                return self.p1
            
            #self.describe_board(self.board)
            #self.board = final
            #c += 1
            #if c % 2 == 0:
            
        print 'uh oh, not supposed to get here'
        return random.choice([self.player1, self.player2, None])
    

    def pygame_event_handler(self):
     
        if self.display:
            pygame.event.pump()
    
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == K_SPACE:
    #                    pygame.quit()
                        pass
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()