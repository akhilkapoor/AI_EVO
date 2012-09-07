'''
@author: Michael Smith, Akhil Kapoor
'''

import random
from Game import Game
from Player import Player
from Heuristic import Heuristic
from copy import deepcopy
from GlobalParams import *

class Evolution(object):
    '''
    classdocs
    '''

    ngenerations = 3
    population_size = 10
    tournament_size = 2
    population = []
    board_size = 20
    statistics = []
    
    # reproduction params
    percent_maintain = 0.5    # number parents to keep
    
    # mutation params
    percent_mutation = 0.2     # number children to mutate
    mutation_factor = 5        # max factor to mutate weights by 

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def run(self):
        
        # initialize population
        self.init_population()
        
        minCrashWeights = []        
        maxCrashWeights = []
        meanCrashWeights = [] 
        
        # run for several generations
        for i in range(self.ngenerations):
            
            crashWeights = []    # not used yet
            regionWeights = []  # not used yet
            
            for j in range(self.population_size):
                weights = self.population[j].heuristic.weights
                
                crashWeights.append(weights[0])
                regionWeights.append(weights[1])    # not used yet
                
            minCrashWeights.append(min(crashWeights))
            maxCrashWeights.append(max(crashWeights))
            meanCrashWeights.append(sum(crashWeights)/float(self.population_size))            
            
            parents = self.parent_selection()
            children = self.reproduce(parents)
            self.population = self.mutate(children)
            
        # set statistics to be analyzed later
        self.statistics.append([minCrashWeights, maxCrashWeights, meanCrashWeights])

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
        tourn_range = range(self.tournament_size)
        
        # selecting next population
        while(len(parents) < self.population_size):
            
            competitors = []
            
            # pick players for tournament
            while(len(competitors) < self.tournament_size):
                p = random.choice(self.population)
                if p not in competitors:
                    competitors.append(p)
                    
            win_counts = [(0) for q in pop_range]   # list of all 0s
            
            # have each player play other players once
            for p1 in tourn_range:
                for p2 in tourn_range:
                    
                    player1 = competitors[p1]
                    player2 = competitors[p2]
                                            
                    # verify AI doesn't play itself
                    if player1 != player2:
                        # player j plays player k
                        g = Game(player1, player2, self.board_size)
                        g.initialize_board()
                        
                        if Global().DEBUG:
                            print 'Player 1 weights: ', player1.heuristic.weights
                            print 'Player 2 weights: ', player2.heuristic.weights
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
        
        n_to_maintain = self.percent_maintain * self.population_size
        
        children = random.sample(parents, int(n_to_maintain))
        
        # crossing over on two random parents' weights
        while(len(children) < self.population_size):
            
            par1 = random.choice(parents)
            par2 = random.choice(parents)
            
            child = deepcopy(par1)
            weights = child.heuristic.weights
            
            for i in range(len(weights)):
                weights[i] = (par1.heuristic.weights[i] + par2.heuristic.weights[i]) / 2

            children.append(child)
        
        return children
    
    def mutate(self, children):
        
        n_to_mutate = int(self.percent_mutation * self.population_size)
        mutant_children = random.sample(children, n_to_mutate)
        
        for i in range(n_to_mutate):
            for weight in mutant_children[i].heuristic.weights:
                weight *= random.random()
        
        return children
    
