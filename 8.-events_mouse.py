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

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event) #pos and button

            if event.button == 1:
                posx, posy = pygame.mouse.get_pos()
                image_rect.center = event.pos #El evento por si solo posee las coordenadas

            if event.button == 3:
                print('Clic derecho')

        if event.type == pygame.MOUSEBUTTONUP:
            pass

    display.fill(WHITE)
    display.blit(image_png, image_rect)

    pygame.display.update()
