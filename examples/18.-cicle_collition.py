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
pygame.display.set_caption('Colisión Circulos')

def create_text(text=''):
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(text, True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, 30)

    return text, text_rect

circle1 = pygame.image.load('resources/sprites/medium_circle.png')
rect1 = circle1.get_rect()
rect1.center = (WIDTH / 2, HEIGHT / 2)

circle2 = pygame.image.load('resources/sprites/medium_circle.png')
rect2 = circle2.get_rect()
rect2.center = (WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()

alph1 = pygame.Surface((rect1.width, rect1.height), pygame.SRCALPHA)   # per-pixel alpha
alph1.fill((0, 0, 0, 50))

alph1_rect = alph1.get_rect()
alph1_rect.center = rect1.center

alph2 = pygame.Surface((rect1.width, rect1.height), pygame.SRCALPHA)   # per-pixel alpha
alph2.fill((0, 0, 0, 50))

alph2_rect = alph2.get_rect()
alph2_rect.center = rect2.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    message = ''

    rect1.center = pygame.mouse.get_pos()
    alph2_rect.center = rect1.center

    display.fill(WHITE)
    display.blit(circle1, rect1)
    display.blit(circle2, rect2)

    display.blit(alph1, alph1_rect)
    display.blit(alph2, alph2_rect)

    pygame.draw.circle(display, BLACK, rect1.center, 5)
    pygame.draw.circle(display, BLACK, rect2.center, 5)

    if rect1.colliderect(rect2):
        message = 'colisión'

    dist = math.hypot(rect1.x - rect2.x, rect1.y - rect2.y)
    if dist < (64 + 64) - 1:
        pygame.draw.line(display, RED, rect1.center, rect2.center, 3)
        message = 'colisión'

    text, text_rect = create_text(message)
    display.blit(text, text_rect)

    clock.tick(60)
    pygame.display.update()
