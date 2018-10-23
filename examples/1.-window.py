import pygame
import sys

pygame.init()
width = 400
height = 500
dimensions = (width, height)

display = pygame.display.set_mode( dimensions )
pygame.display.set_caption('Hola Mundo!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
