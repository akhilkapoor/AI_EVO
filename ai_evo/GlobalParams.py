'''
@author: Akhil Kapoor, Michael Smith
'''

DEBUG = False

# Evolutionary Params
NUM_GENERATIONS = 5
POP_SIZE = 30
TOURN_SIZE = 5
PERCENT_MAINTAIN = 0.2  # number parents to keep
PERCENT_MUTATION = 0.2  # number children to mutate
MUTATION_FACT = 50      # max factor to mutate weights by
BOARD_SIZE = 12

# Game Params
DISPLAY = False
FPS = 10    # frames per second setting, probably limited to about 25
WINDOW_SIZE = 600
RESIZE_FACTOR = WINDOW_SIZE/BOARD_SIZE

# Colors
WHITE   = (255, 255, 255)
L_GREEN = (  0, 220,   0)
N_BLUE  = (  0,   0, 128)
PURPLE  = (200,   0, 200)
RED     = (255,   0,   0)

def set_display(display):
    global DISPLAY
    DISPLAY = display
    
def update_resize_factor():
    global RESIZE_FACTOR
    RESIZE_FACTOR = WINDOW_SIZE/BOARD_SIZE
    
def set_board_size(size):
    global BOARD_SIZE
    BOARD_SIZE = size