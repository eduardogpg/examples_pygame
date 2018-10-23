import pygame
import sys

pygame.init()

WIDTH = 288
HEIGHT = 512

#RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
FPS = 30

FONT = pygame.font.Font('Roboto/Roboto-BlackItalic.ttf', 24)

def get_text(text=''):
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (WIDTH/ 2, 20)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Title!')

image_png = pygame.image.load('sprites/redbird-upflap.png')
image_posx = 100
image_posy = 100

pygame.mixer.music.load('sounds/Death.mp3')
pygame.mixer.music.play(-1, 0.0) #loops and start

contador = 0
text_rect = get_text('Contador ' + str(contador))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound = pygame.mixer.Sound('sounds/swoosh.wav')
                sound.play()
                text_rect = get_text('Contador ' + str(contador + 1))

    display.fill(WHITE)
    display.blit(image_png, (image_posx, image_posy))
    display.blit(text_surface, text_rect)

    pygame.display.update()
