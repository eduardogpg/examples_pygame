import pygame
import sys
import os

WIDTH = 400
HEIGHT = 512
WHITE = (255, 255, 255)

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Movimiento por mouse')

image_png = pygame.image.load('resources/sprites/medium_circle.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    image_rect.center = pygame.mouse.get_pos()

    display.fill(WHITE)
    display.blit(image_png, image_rect)

    clock.tick(60)
    pygame.display.update()
