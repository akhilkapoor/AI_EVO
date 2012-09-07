'''
@author: Michael Smith, Akhil Kapoor
'''
from Evolution import Evolution
from Game import Game
from Player import Player
from Heuristic import Heuristic
from matplotlib import pyplot as plt

class TronEvo(object):
    '''
    classdocs
    '''

    def __init__(self,params):
        '''
        Constructor
        '''
        
    def run(self):
        tronEvo = self.run_evolution()
        self.run_statistics(tronEvo)

    def run_evolution(self):
        tronEvo = Evolution(None)
        tronEvo.run()
        return tronEvo

    def test_game(self):
        p1 = Player()
        p1.name = 'p1'
        p1.pos = [5,2]
        p1.heuristic = Heuristic()
        p2 = Player()
        p2.name = 'p2'
        p2.pos = [5,7]
        p2.heuristic = Heuristic()
        g = Game(p1, p2, 20)
        g.initialize_board(10)
        g.describe_board(g.board)
        g.play()
        
    def run_statistics(self, tronEvo):
        
        stats = tronEvo.statistics
        ngen = tronEvo.ngenerations
        
        for i in range(4):
            plt.figure(i)
            plt.plot(range(ngen), stats[i][0], label='Minimum Weight Value')
            plt.plot(range(ngen), stats[i][0], label='Maximum Weight Value')
            plt.plot(range(ngen), stats[i][0], label='Mean Weight Value')
            plt.xlabel('Generation')
            plt.ylabel('Weight Value')
            plt.legend()
            plt.title('Final weight value of ' + str(stats[i][-1]))
            plt.show()
