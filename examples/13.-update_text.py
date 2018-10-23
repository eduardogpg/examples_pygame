import pygame
import sys
import os

WIDTH = 288
HEIGHT = 512
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

ROBOTO_FONT = pygame.font.Font('resources/Roboto/Roboto-Italic.ttf', 18)

def create_text(text='Nothing', centerx=0, centery=0, color=(0, 0, 0)):
    text = ROBOTO_FONT.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (centerx, centery)

    return text, text_rect

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

image_png = pygame.image.load('resources/sprites/redbird-upflap.png')
image_rect = image_png.get_rect()
image_rect.center = (WIDTH / 2, HEIGHT / 2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    format = 'pos x : {} - pos y : {}'.format(image_rect.centerx, image_rect.centery )
    text, text_rect = create_text(format, WIDTH / 2, 15 ,BLACK)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        image_rect.y -= 4
    if pressed[pygame.K_d]:
        image_rect.x += 4
    if pressed[pygame.K_a]:
        image_rect.x -= 4
    if pressed[pygame.K_s]:
        image_rect.y += 4

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

    clock.tick(30)
    pygame.display.update()
