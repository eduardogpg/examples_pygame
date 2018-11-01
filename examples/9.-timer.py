import pygame
import sys

pygame.init()

WIDTH = 288
HEIGHT = 512

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (134,45,83)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Timer')

seconds = 0

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Timer : ' + str(seconds), True, RED)

text_rect = text.get_rect()
text_rect.center = (WIDTH / 2, HEIGHT / 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    seconds = int(pygame.time.get_ticks() / 1000) #Obtenemos los milisegundos
    text = font.render('Timer : ' + str(seconds), True, RED)

    display.fill(WHITE)
    display.blit(text, text_rect)

    pygame.display.update()
