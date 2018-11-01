import math
import pygame
import sys
import os

WIDTH = 600
HEIGHT = 500
WHITE = (255, 255, 255)
RED = (134,45,83)
BLACK = (0, 0, 0)

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Colisión mask')

def create_text(text=''):
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(text, True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, 30)

    return text, text_rect

circle = pygame.image.load('resources/sprites/medium_circle.png')
circle_rect = circle.get_rect()
circle_rect.center = (WIDTH / 2, HEIGHT / 2)

circle_alpha = pygame.Surface((rect1.width, rect1.height), pygame.SRCALPHA)
circle_alpha.fill((0, 0, 0, 50))

circle_alpha_rect = circle_alpha.get_rect()
circle_alpha_rect.center = rect1.center

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    message = ''

    rect1.center = pygame.mouse.get_pos()
    alph2_rect.center = rect1.center

    display.fill(WHITE)

    display.blit(circle, circle_rect)
    display.blit(circle_alpha, circle_alpha_rect)

    text, text_rect = create_text(message)
    display.blit(text, text_rect)

    clock.tick(60)
    pygame.display.update()
