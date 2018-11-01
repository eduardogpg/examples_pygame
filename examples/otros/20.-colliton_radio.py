import math
import sys
import pygame
from pygame.math import Vector2 as vector

pygame.init()

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (122,41,101)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Collitions circles')

radio = 100

rect1 = pygame.Rect(WIDTH / 2, HEIGHT / 2, 1, 1)
rect2 = pygame.Rect(0, 0, 1, 1)

while True:

    display.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        rect2.center = pygame.mouse.get_pos()

        pygame.draw.circle( display, BLACK, rect1.center, radio, 4)
        pygame.draw.circle( display, BLACK, rect2.center, radio, 4)

        color = BLACK

        dist = math.hypot(rect1.x - rect2.x, rect1.y - rect2.y)
        if dist < (radio  + radio) - 1:
            color = RED

        pygame.draw.line(display, color, rect1.center, rect2.center, 3)

        pygame.draw.circle( display, PURPLE, rect1.center, 5)
        pygame.draw.circle( display, PURPLE, rect2.center, 5)

        pygame.display.update()
