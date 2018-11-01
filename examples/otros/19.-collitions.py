import sys
import pygame

pygame.init()

WIDTH = 500
HEIGHT = 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Collitions')

image1 = pygame.Surface( (40, 40) )
image1.fill(BLUE)

rect1 = image1.get_rect()
rect1.center =  (100, 100)

image2 = pygame.Surface( (120, 120 ))
image2.fill(GREEN)

rect2 = image2.get_rect()
rect2.center =  (WIDTH / 2, HEIGHT / 2)

default_font = pygame.font.Font('freesansbold.ttf', 24)

def create_text(text='Nothing', centerx=0, centery=0, color=(0, 0, 0)):
    text = default_font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (centerx, centery)

    return text, text_rect

while True:

    display.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        rect1.center = pygame.mouse.get_pos()

        if rect1.colliderect(rect2):
            image1.fill(RED)
        else:
            image1.fill(BLUE)

        text, text_rect = create_text("Right > " + str(rect1.right), WIDTH / 2, 15 ,BLACK)
        display.blit(text, text_rect)

        display.blit(image1, rect1)
        display.blit(image2, rect2)

        text, text_rect = create_text("Left >" + str(rect2.left), WIDTH / 2, 40 ,BLACK)
        display.blit(text, text_rect)

        pygame.display.update() # ro display.flip()
