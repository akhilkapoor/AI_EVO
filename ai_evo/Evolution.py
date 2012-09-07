'''
@author: Michael Smith, Akhil Kapoor
'''

import random
import Game
from ai_evo import Player
from ai_evo.Heuristic import Heuristic

class Evolution(object):
    '''
    classdocs
    '''

    ngenerations = 100
    population_size = 100
    tournament_size = 5
    population = None
    board_size = 400

    def __init__(self,params):
        '''
        Constructor
        '''
        pass
        
    def run(self):
        
        # initialize population
        self.population = self.init_population()
        
        # run for several generations
        for i in range(self.ngenerations):
            
            parents = self.parent_selection()
            children = self.reproduce(parents)
            self.population = self.mutatate(children)
            
        pass
    
    def init_population(self):
        while(len(self.population) < self.population_size):
            p = Player()
            p.heuristic = Heuristic()
            p.heuristic.weights = [random.randint(-100,100) for i in range(4)]
            self.population.append(p)
        pass
    
    def parent_selection(self):
        # only 'most fit' players are selected for reproduction
        parents = []
        pop_range = range(self.population_size)
        
        # selecting next population
        while(len(parents) < self.population_size):
            
            competitors = []
            
            # pick players for tournament
            while(len(competitors < self.tournament_size)):
                p = random.choice(self.population)
                if p not in competitors:
                    competitors.append(p)
                    
            win_counts = [(0) for q in pop_range]   # list of all 0s
            
            # have each player play other players once
            for p1 in pop_range:
                for p2 in pop_range:
                    
                    player1 = competitors[p1]
                    player2 = competitors[p2]
                                            
                    # verify AI doesn't play itself
                    if player1 != player2:
                        # player j plays player k
                        g = Game(player1, player2, self.board_size)
                        winner = g.play()
                        
                        # only increment counts if true winner (no draws)
                        if player1 == winner:
                            win_counts[p1] = win_counts[p1] + 1
                        elif player2 == winner:
                            win_counts[p2] = win_counts[p2] + 1
            
            # append best Player to 'parents'
            best_player_index = win_counts.index(max(win_counts))
            best_player = competitors[best_player_index]
            parents.append(best_player)
        
        return parents
    
    
    def reproduce(self, parents):
        children = []
        
        # do some sort of crossover
        
        return children
    
    def mutate(self, children):
        mutations = []
        
        # do some form of mutation
        
        return mutations
    