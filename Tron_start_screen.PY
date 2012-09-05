import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 40 # frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Tron!')

GRAY    = (128, 128, 128)
L_GREEN = (  0, 220,   0)
N_BLUE  = (  0,   0, 128)
PURPLE  = (200,   0, 200)

x1 = 100
y1 = 100
x2 = 300
y2 = 200
dx = 2
dy = 0
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('TRON!', True, N_BLUE, GRAY)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
DISPLAYSURF.blit(textSurfaceObj, textRectObj)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP and event.key == K_ESCAPE:
            exit()
        
    if x1 < 295:
        x1 = x1+dx
        x2 = x2-dx

    pygame.draw.line(DISPLAYSURF, L_GREEN, (x1, y1), (x1+5, y1), 5)
    pygame.draw.line(DISPLAYSURF, PURPLE, (x2, y2), (x2-5, y2), 5)
    pygame.display.update()
    fpsClock.tick(FPS)
    
exit()
