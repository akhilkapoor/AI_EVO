import io

# Game = {
#   player {
#       position : [x, y]
#       direction : north, south, east, west  // decide next or current
#       color : Blue/Pink
#       movesMade : [left, straight, right] // computer can have straight, human cannot
#       previos_position : [x, y]
#        }
#   }
#   board : [400x400] of ' '

def initialBoard(n):
    board = []
    for i in range(n):
        board.append(["."]*n)
    return board

# Any collision - head-on, next-move, tail, wall
def goal(Game, player):
    return 1

#
def applyMove(move, oldGame, player):
    return newGame

def applicableMoves(player):
    return 'Direction'

def describeBoard(board):
    print board

def describeMove(move):
    print move

def play():
    print 'play'

def randomMove():
    # choose left or right or keep going

def userMove():
    # input from somewhere

def main(args):
    print 'MAIN'

if __name__ == "__main__":
    main(sys.argv)
