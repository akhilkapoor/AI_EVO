'''
@author: Michael Smith, Akhil Kapoor
'''
from Evolution import Evolution
from Game import Game
from Player import Player
from Heuristic import Heuristic
from GlobalParams import *

from matplotlib import pyplot as plt
import random

class TronEvo(object):

    def __init__(self):
        '''
        Constructor
        '''
        
    def run(self):
        tronEvo = self.run_evolution()
        self.run_statistics(tronEvo)        
        self.play_old_vs_new(tronEvo)

    def run_evolution(self):
        tronEvo = Evolution()
        tronEvo.run()
        return tronEvo

    def test_game(self):
        p1 = Player()
        p1.name = 'p1'
        p1.pos = [BOARD_SIZE/2,BOARD_SIZE/4]
        p1.heuristic = Heuristic()
        p1.heuristic.weights.append(1000)
        p1.heuristic.weights.append(20)
        
        p2 = Player()
        p2.name = 'p2'
        p2.pos = [BOARD_SIZE/2,3*BOARD_SIZE/4]
        p2.heuristic = Heuristic()
        p2.heuristic.weights.append(-20)
        p2.heuristic.weights.append(20)
        g = Game(p1, p2, BOARD_SIZE)
        g.display = True
        g.initialize_board()
        
        #g.describe_board(g.board)
        
        g.play()
        
    def play_old_vs_new(self,tronEvo):

        # redefine some globals
        globals()['BOARD_SIZE'] = 20
        globals()['DISPLAY'] = True
            
        player1 = random.choice(tronEvo.last_pop)
        player2 = random.choice(tronEvo.last_pop)
        
        print 'Player 1 weights:', player1.heuristic.weights
        print 'Player 2 weights:', player2.heuristic.weights

        g = Game(player1, player2, BOARD_SIZE)
        g.display = DISPLAY
        g.initialize_board()
        
        g.play(True)
        raw_input('Hit enter to exit..')

    def run_statistics(self, tronEvo):
        
        stats = tronEvo.statistics
        generation_range = range(NUM_GENERATIONS)
        
        weight_types = ['Crashing', 'Distance from Opponent', 'Region Difference']
        
        for i,stat in enumerate(stats):
            plt.figure()
            plt.plot(generation_range, stat[0], label='Min')
            plt.plot(generation_range, stat[1], label='Max')
            plt.plot(generation_range, stat[2], label='Mean')
            plt.xlabel('Generation')
            plt.ylabel('Weight Value')
            plt.legend()
            plt.title('Weight evolution for ' + weight_types[i] + ' over time')
            plt.draw()
        
        if len(stats) > 0:
            plt.show()
    
tron = TronEvo() 
tron.run()
#tron.test_game()