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

pygame.mixer.music.load('resources/sounds/Haggstrom.mp3')
pygame.mixer.music.set_volume(1.0) #0.0 - 1.0
pygame.mixer.music.play(-1, 0.0) #How many times and when start

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    seconds = int(pygame.time.get_ticks() / 1000) #Obtenemos los milisegundos
    text = font.render('Timer : ' + str(seconds), True, RED)

    if seconds == 5:
        #rewind
        #pause
        #stop
        #pygame.mixer.music.rewind()
        pygame.mixer.music.fadeout(5000) #milisegundos

    display.fill(WHITE)
    display.blit(text, text_rect)

    pygame.display.update()
