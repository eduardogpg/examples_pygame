import pygame
import sys

pygame.init()

WIDTH = 288
HEIGHT = 512

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (134,45,83)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Surface')

default_font = pygame.font.Font('freesansbold.ttf', 32)

#render(text, antialias, color, background=None) -> Surface
text_default = default_font.render('Hola Mundo!', True, RED)
text_default_rect = text_default.get_rect()
text_default_rect.center = (WIDTH / 2, 50)

roboto_font = pygame.font.Font('resources/Roboto/Roboto-BlackItalic.ttf', 32)
text_roboto = roboto_font.render('Hola Mundo!', True, RED)
text_roboto_rect = text_default.get_rect()
text_roboto_rect.center = (WIDTH / 2, 100)

#Returns the full path to a font file on the system.
#Error load fonts
#https://github.com/expyriment/expyriment/issues/123
path_font = pygame.font.match_font('arial')
print(path_font)

system_font = pygame.font.Font(path_font, 32)
text_system = system_font.render('Hola Mundo!', True, RED)
text_system_rect = text_system.get_rect()
text_system_rect.center = (WIDTH / 2, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)
    display.blit(text_default, text_default_rect)
    display.blit(text_roboto, text_roboto_rect)
    display.blit(text_system, text_system_rect)

    pygame.display.update()
