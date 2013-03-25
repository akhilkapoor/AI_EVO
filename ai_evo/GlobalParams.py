'''
@author: Akhil Kapoor, Michael Smith
'''

# to change values at run-time use:
#    globals()['VAR_NAME'] = VALUE

DEBUG = False

# Evolutionary Params
NUM_GENERATIONS = 4
POP_SIZE = 14
TOURN_SIZE = 3
NUM_WEIGHTS = 3         # number of weights to initialize with
PERCENT_MAINTAIN = 1  # number parents to keep
PERCENT_MUTATION = 0  # number children to mutate
MUTATION_FACT = 50      # max factor to mutate weights by
BOARD_SIZE = 12

# Game Params
DISPLAY = True
FPS = 20    # frames per second setting, probably limited to about 25
WINDOW_SIZE = 600
RESIZE_FACTOR = WINDOW_SIZE/BOARD_SIZE

# Colors
WHITE   = (255, 255, 255)
L_GREEN = (  0, 220,   0)
N_BLUE  = (  0,   0, 128)
PURPLE  = (200,   0, 200)
RED     = (255,   0,   0)