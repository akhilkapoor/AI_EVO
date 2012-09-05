Project Goals: 
Developing an AI player for the Tron Game that can play competitively against its opponents. Also providing a graphical representation of the game to allow humans to play against the final AI.

Evolutionary Approach: 
Starting with an initial population of nodes, each node contains a set of randomized weights for different behavioral attributes. For small population sizes, each node will compete with every other node. We also intend to experiment with a tournament selection instead for larger populations. At the end of each generation, nodes should be assigned a score based on their overall performance against their opponents, which may be as simple as a count of wins vs losses. 

AI Behavior: 
Each Tron AI developed is independent of all others at the beginning of the simulation. Over time, better scoring agents will be used to determine the next generation of agents. Weights of each agent include any of the following:
* Number of lookaheads in the heuristic
* Proximity to walls
* Percentage of current board accessible
A reproduction method may not make sense in this representation, but the simulation could benefit from mutation. Mutation would involve taking a previous set of weights, and adding some random factor to either one, or several of the weights. The rate of mutation is also an important characteristic we will have to experiment with. 