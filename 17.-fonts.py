import pygame
import sys

pygame.init()

WIDTH = 288
HEIGHT = 512

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#freesansbold.ttf #fuente que viene con pygame
FONT = pygame.font.Font('Roboto/Roboto-BlackItalic.ttf', 24)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Example')

#una superficie en la cual pintar
text_surface = FONT.render('Movimiento', True, BLACK) #https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render

image_png = pygame.image.load('sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    display.fill(WHITE)
    display.blit(image_png, image_rect)

    pygame.display.update()
