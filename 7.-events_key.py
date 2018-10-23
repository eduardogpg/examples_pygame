import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512
WHITE = (255, 255, 255)

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

        if event.type == pygame.KEYDOWN:
            print(event) #unicode, key

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Izquierda")

            if event.key == pygame.K_RIGHT or event.key == pygame.K_w:
                print("Derecha")

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Arriba")

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Abajo")

        if event.type == pygame.KEYUP:
            pass

    display.fill(WHITE)
    display.blit(image_png, image_rect)

    pygame.display.update()
