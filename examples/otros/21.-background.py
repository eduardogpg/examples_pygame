import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512
WHITE = (255, 255, 255)
#RGB
DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

background = pygame.image.load('resources/sprites/background-night.png')
background_rect = background.get_rect()

pos_x1 = 0
pos_x2 = background_rect.width

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        image_rect.x -= 5

    if pressed[pygame.K_d]:
        image_rect.x += 5

    pos_x1 -= 1
    pos_x2 -= 1

    display.blit(background, (pos_x1, 0))
    display.blit(background, (pos_x2, 0))

    display.blit(image_png, image_rect)

    if pos_x1 < - background_rect.width:
        pos_x1 = background_rect.width

    if pos_x2 < - background_rect.width:
        pos_x2 = background_rect.width

    pygame.display.update()
