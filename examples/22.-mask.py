import sys
import pygame

pygame.init()


def create_text(text='Nothing', centerx=0, centery=0, color=(0, 0, 0)):
    default_font = pygame.font.Font('freesansbold.ttf', 24)

    text = default_font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (centerx, centery)

    return text, text_rect

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Cargar imagenes!')

image_coin = pygame.image.load('resources/sprites/coin.png')
image_coin_rect = image_coin.get_rect()
image_coin_rect.center =  (WIDTH / 2, HEIGHT / 2)

alph = pygame.Surface((image_coin_rect.width, image_coin_rect.height),
                        pygame.SRCALPHA)   # per-pixel alpha
alph.fill((255,255,255,100))
alph_rect = alph.get_rect()
alph_rect.center = image_coin_rect.center

player_image = pygame.image.load('resources/sprites/player1.png')
player_rect = player_image.get_rect()

player_mask = pygame.mask.from_surface(player_image)
image_coin_mask = pygame.mask.from_surface(image_coin)

while True:
    #pygames masks use only 1 bit per pixel.
    #This makes it very quick to check for collisions.
    #As you can compare 32 pixels with one integer compare.
    #Masks use bounding box collision first - to speed things up.

    display.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_rect.center = pygame.mouse.get_pos()

    display.blit(player_image, player_rect)
    display.blit(image_coin, image_coin_rect)
    display.blit(alph, alph_rect)

    if player_rect.colliderect(image_coin_rect):
        pass
        
    m = ''
    result = player_mask.overlap(image_coin_mask, (0, 1) )
    if result:
        m = '' + str(result)
        pygame.draw.circle(display, (225, 0, 0), result, 2 )

    text, text_rect = create_text("Collition : " +m, WIDTH / 2, 15 , WHITE)
    display.blit(text, text_rect)

    pygame.display.flip()
