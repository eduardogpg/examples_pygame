import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512

#RGB
WHITE = (255, 255, 255)

DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

#RGB
WHITE = (255, 255, 255)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
#image_posx = 100
#image_posy = 100

image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

print(image_rect.x)
print(image_rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)

    #Qué se pintará, Donde se pintara
    display.blit(image_png, image_rect)
    pygame.display.update()
