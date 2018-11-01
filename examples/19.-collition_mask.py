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
pygame.display.set_caption('Mask!')

circle = pygame.image.load('resources/sprites/medium_circle.png').convert_alpha()
circle_mask = pygame.mask.from_surface(circle)
circle_rect = circle.get_rect()
circle_rect.center = (WIDTH / 2, HEIGHT / 2)

rectangle = pygame.image.load('resources/sprites/small_rectangle.png').convert_alpha()
rectangle_mask = pygame.mask.from_surface(rectangle)
rectangle_rect = rectangle.get_rect()

def create_text(text=''):
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(text, True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, 30)

    return text, text_rect

#Circle

#rectangle

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rectangle_rect.center = pygame.mouse.get_pos()
    message = ''

    offset = ( rectangle_rect.x - circle_rect.x , rectangle_rect.y - circle_rect.y  )
    result = circle_mask.overlap(rectangle_mask, offset)
    if result:
        message = 'Colisión'
    
    display.fill(WHITE)
    display.blit(circle, circle_rect)
    display.blit(rectangle, rectangle_rect)

    text, rect = create_text(message)
    display.blit(text, rect)

    clock.tick(60)
    pygame.display.update()
