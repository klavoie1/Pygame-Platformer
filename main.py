import pygame
import sys
from settings import *
from level import Level

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
level = Level(map_level, window)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill('black')
    level.run() 

    pygame.display.update()
    clock.tick(60)