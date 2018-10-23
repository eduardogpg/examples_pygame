import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

pygame.mixer.music.load('resources/sounds/Haggstrom.mp3')
pygame.mixer.music.play(-1, 0.0)

sound_jump = pygame.mixer.Sound('resources/sounds/swoosh.wav')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_jump.play()

    display.fill(WHITE)
    display.blit(image_png, image_rect)

    clock.tick(30)
    pygame.display.update()
