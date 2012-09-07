'''
@author: Michael Smith, Akhil Kapoor
'''

import random
import Game
from Player import Player
from Heuristic import Heuristic

class Evolution(object):
    '''
    classdocs
    '''

    ngenerations = 100
    population_size = 100
    tournament_size = 5
    population = None
    board_size = 400
    statistics = []

    def __init__(self,params):
        '''
        Constructor
        '''
        pass
        
    def run(self):
        
        # initialize population
        self.population = self.init_population()
        
        minWinWeights = []        
        maxWinWeights = []
        meanWinWeights = [] 
        
        # run for several generations
        for i in range(self.ngenerations):
            
            winWeights = []
            lossWeights = []    # not used yet
            regionWeights = []  # not used yet
            
            for j in range(self.population_size):
                weights = self.population[j]
                
                winWeights.append(weights[0])
                lossWeights.append(weights[1])      # not used yet
                regionWeights.append(weights[2])    # not used yet
                
            minWinWeights.append(min(winWeights))
            maxWinWeights.append(max(winWeights))
            meanWinWeights.append(sum(winWeights)/float(self.population_size))            
            
            parents = self.parent_selection()
            children = self.reproduce(parents)
            self.population = self.mutatate(children)
            
        # set statistics to be analyzed later
        self.statistics.append([minWinWeights, maxWinWeights, meanWinWeights])

    def init_population(self):
        while(len(self.population) < self.population_size):
            p = Player()
            p.heuristic = Heuristic()
            p.heuristic.weights = [random.randint(-100,100) for i in range(4)]
            self.population.append(p)
    
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
    
