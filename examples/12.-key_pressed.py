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

message = 'Presione un tecla'

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

    text, text_rect = create_text(message)
    display.blit(text, text_rect)

    pygame.display.update()
