import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512

#RGB
WHITE = (255, 255, 255)
RED = (134,45,83)

DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

def create_text(text=''):
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(text, True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 2)

    return text, text_rect


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)

    posx, posy = pygame.mouse.get_pos()
    message = 'x : ' + str(posx) + ' / y :' + str(posy)

    text, text_rect = create_text(message)
    display.blit(text, text_rect)

    pygame.display.update()
