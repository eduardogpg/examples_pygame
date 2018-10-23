import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512

#RGB
WHITE = (255, 255, 255)

DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

clock = pygame.time.Clock()

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    posx, posy = pygame.mouse.get_pos()
    image_rect.center = (posx, posy)

    display.fill(WHITE)
    display.blit(image_png, image_rect)

    clock.tick(60)
    pygame.display.update()
