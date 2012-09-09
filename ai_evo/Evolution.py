'''
@author: Michael Smith, Akhil Kapoor
'''

import random
import numpy as np
from Game import Game
from Player import Player
from Heuristic import Heuristic
from copy import deepcopy
from GlobalParams import *

class Evolution(object):
    
    first_pop = []
    last_pop = []
    population = []
    statistics = []

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def run(self):
        
        # initialize population
        self.init_population()
        
        self.first_pop = deepcopy(self.population)
        
        minCrashWeights = []        
        maxCrashWeights = []
        meanCrashWeights = [] 
        
        minDistanceWeights = []
        maxDistanceWeights = []
        meanDistanceWeights = []
        
        minRegionWeights = []
        maxRegionWeights = []
        meanRegionWeights = []
        
        # run for several generations
        for i in range(NUM_GENERATIONS):
            
            print 'Generation', i
            
            crashWeights = []
            distanceWeights = []
            regionWeights = []
            
            for j in range(POP_SIZE):
                weights = self.population[j].heuristic.weights
                
                crashWeights.append(weights[0])
                distanceWeights.append(weights[1])
                regionWeights.append(weights[2])
                
            self.append_stats(minCrashWeights, maxCrashWeights, meanCrashWeights, crashWeights)
            self.append_stats(minDistanceWeights, maxDistanceWeights, meanDistanceWeights, distanceWeights)
            self.append_stats(minRegionWeights, maxRegionWeights, meanRegionWeights, regionWeights)
            
            parents = self.parent_selection()
            children = self.reproduce(parents)
            self.population = self.mutate(children)
            
        # set statistics to be analyzed later
        self.statistics.append([minCrashWeights, maxCrashWeights, meanCrashWeights])
        self.statistics.append([minDistanceWeights, maxDistanceWeights, meanDistanceWeights])
        self.statistics.append([minRegionWeights, maxRegionWeights, meanRegionWeights])
        
        self.last_pop = deepcopy(self.population)
        
    def append_stats(self, min_w, max_w, mean_w, weight_vals):
        min_w.append(min(weight_vals))
        max_w.append(max(weight_vals))
        mean_w.append(sum(weight_vals)/float(POP_SIZE))

    def init_population(self):
        while(len(self.population) < POP_SIZE):
            p = Player()
            p.heuristic = Heuristic()
            p.heuristic.weights = [random.randint(-100,100) for i in range(NUM_WEIGHTS)]
            self.population.append(p)
    
    def parent_selection(self):
        # only 'most fit' players are selected for reproduction
        parents = []
        pop_range = range(POP_SIZE)
        tourn_range = range(TOURN_SIZE)
        
        # selecting next population
        while(len(parents) < POP_SIZE):
            
            # take random sample of players for tournament
            competitors = random.sample(self.population, TOURN_SIZE) 
                               
            win_counts =  np.array([0]*TOURN_SIZE)  # list of all 0s
            
            # have each player play other players once
            for p1 in tourn_range:
                for p2 in tourn_range:
                    
                    player1 = competitors[p1]
                    player2 = competitors[p2]
                                            
                    # verify AI doesn't play itself
                    if player1 != player2:
                        # player j plays player k
                        g = Game(player1, player2, BOARD_SIZE)
                        g.initialize_board()
                        
                        if DEBUG:
                            print 'Player 1 weights: ', player1.heuristic.weights
                            print 'Player 2 weights: ', player2.heuristic.weights
                        winner = g.play()
                        
                        # only increment counts if true winner (no draws)
                        if player1 == winner:
                            win_counts[p1] += 1
                        elif player2 == winner:
                            win_counts[p2] += 1
            
            # find all 'best players'
            best_player_indices = np.where(win_counts == (max(win_counts)))[0]
        
            # if more than one 'best player' is found, choose randomly
            best_player = competitors[random.choice(best_player_indices)]
            parents.append(best_player)
        
        return parents
    
    
    def reproduce(self, parents):        
        n_to_maintain = PERCENT_MAINTAIN * POP_SIZE
        
        children = random.sample(parents, int(n_to_maintain))
        
        # crossing over on two random parents' weights
        while(len(children) < POP_SIZE):
            
            par1 = random.choice(parents)
            par2 = random.choice(parents)
            
            child = deepcopy(par1)
            weights = child.heuristic.weights
            
            for i in range(len(weights)):
                weights[i] = (par1.heuristic.weights[i] + par2.heuristic.weights[i]) / 2

            children.append(child)
        
        return children
    
    def mutate(self, children):
        
        n_to_mutate = int(PERCENT_MUTATION * POP_SIZE)
        mutant_children = random.sample(children, n_to_mutate)
        
        for i in range(n_to_mutate):
            for weight in mutant_children[i].heuristic.weights:
                weight *= random.randrange(-MUTATION_FACT,MUTATION_FACT)
        
        return children