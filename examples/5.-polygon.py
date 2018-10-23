import pygame
import sys

pygame.init()

WIDTH = 400
HEIGHT = 500

#RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Poligonos!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)

    pygame.draw.polygon(display, GREEN, (
        (146, 0),
        (291, 106),
        (236, 277),
        (56, 277),
        (0, 106)
    ))

    pygame.draw.polygon(display, BLUE, (
        (0, 400) , (100, 300) , (200, 400)
    ))

    pygame.display.update()
