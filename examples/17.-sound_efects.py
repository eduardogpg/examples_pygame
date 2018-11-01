import pygame
import sys
import os

WIDTH = 600
HEIGHT = 500
WHITE = (255, 255, 255)
RED = (134,45,83)

pygame.init()

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Colisión rectangulos')

def create_text(text=''):
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render(text, True, RED)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH / 2, 50)

    return text, text_rect

rectangle = pygame.image.load('resources/sprites/small_rectangle_red.png')
rectangle_rect = rectangle.get_rect()
rectangle_rect.center = (WIDTH / 2, HEIGHT / 2)

image_png = pygame.image.load('resources/sprites/small_rectangle.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    message = ''

    image_rect.center = pygame.mouse.get_pos()

    display.fill(WHITE)
    display.blit(image_png, image_rect)
    display.blit(rectangle, rectangle_rect)

    if image_rect.colliderect(rectangle_rect):
        efect = pygame.mixer.Sound('resources/sounds/swoosh.wav')
        efect.play()

    text, text_rect = create_text(message)
    display.blit(text, text_rect)

    clock.tick(60)
    pygame.display.update()
