import pygame
import sys
import os

WIDTH = 400
HEIGHT = 512

WHITE = (255, 255, 255)
RED = (134,45,83)

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Eventos del teclado!')

def create_text(text=''):
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(text, True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, HEIGHT / 2)

    return text, text_rect

message = 'Eventos del teclado'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event) #pos and button

            print(event.pos)

            if event.button == 1:
                posx, posy = pygame.mouse.get_pos()

                message = 'Izquierda'

            if event.button == 2:
                message = 'Centro'

            if event.button == 3:
                message = 'Derecha'

            if event.button == 4:
                message = 'Arriba'

            if event.button == 5:
                message = 'Abajo'

        if event.type == pygame.MOUSEBUTTONUP:
            pass

    display.fill(WHITE)

    text, text_rect = create_text(message)
    display.blit(text, text_rect)

    pygame.display.update()
