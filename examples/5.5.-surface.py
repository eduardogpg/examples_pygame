import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512

#RGB
WHITE = (255, 255, 255)
RED = (134,45,83)

DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

#RGB
WHITE = (255, 255, 255)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Surface')

surface = pygame.Surface((200, 200))
surface.fill(RED)

surface_rect = surface.get_rect()
surface_rect.center = (WIDTH / 2, HEIGHT / 2)

#https://www.pygame.org/docs/ref/surface.html
rectangle = pygame.Rect((surface_rect.width / 2) - 25,
                        (surface_rect.height / 2) - 25,
                        50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)

    pygame.draw.rect(surface, WHITE, rectangle)

    display.blit(surface, surface_rect)
    pygame.display.update()
