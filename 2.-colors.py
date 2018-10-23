import pygame
import sys

pygame.init()

WIDTH = 400
HEIGHT = 500

#Existen dos formas de representar a un color, por una tupla o un objeto.

#RGB
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Colores!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)
    pygame.display.update()
