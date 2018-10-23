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

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("Arriba")
    if pressed[pygame.K_a]:
        print("Izquierda")
    if pressed[pygame.K_s]:
        print("Abajo")
    if pressed[pygame.K_d]:
        print("Derecha")

    display.fill(WHITE)
    display.blit(image_png, image_rect)

    pygame.display.update()
