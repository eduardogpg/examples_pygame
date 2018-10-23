import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Fuentes!')

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()

default_font = pygame.font.Font('freesansbold.ttf', 24)
roboto_font = pygame.font.Font('resources/Roboto/Roboto-Italic.ttf', 18)

text = roboto_font.render('Hello World', True, BLACK)
text_rect = text.get_rect()
text_rect.center = (WIDTH / 2, text_rect.height - 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        image_rect.y -= 5
    if pressed[pygame.K_d]:
        image_rect.x += 5
    if pressed[pygame.K_a]:
        image_rect.x -= 5
    if pressed[pygame.K_s]:
        image_rect.y += 5

    if image_rect.left < 0:
        image_rect.left = 0

    if image_rect.top < 0:
        image_rect.top = 0

    if image_rect.bottom > HEIGHT:
        image_rect.bottom = HEIGHT

    if image_rect.right > WIDTH:
        image_rect.right = WIDTH

    display.fill(WHITE)
    display.blit(image_png, image_rect)
    display.blit(text, text_rect)#display.blit(text, (70, 0))

    clock.tick(60)
    pygame.display.update()
