'''
@author: Michael Smith, Akhil Kapoor
'''
from Evolution import Evolution
from Game import Game
from Player import Player
from Heuristic import Heuristic

class TronEvo(object):
    '''
    classdocs
    '''

    def __init__(self,params):
        '''
        Constructor
        '''
        
    def run(self):
        pass
        
    def runEvolution(self):
        tronEvo = Evolution
        tronEvo.run()
		
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
