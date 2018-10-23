import pygame
import sys

pygame.init()

#RGB
WHITE = (255, 255, 255)

display = pygame.display.set_mode( (400, 500) )
pygame.display.set_caption('Title!')

fps_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)

    pygame.draw.rect(display, (255, 0, 0), (10, 20, 50, 80))

    #surfeca, color, pos first point, pos second point
    pygame.draw.line(display, (0, 0, 255), (120, 60), (120, 120), 2)

    #surfeca, color, pos center, radius
    pygame.draw.circle(display, (0, 255, 0), (120, 300), 40)

    pygame.display.update()
    fps_clock.tick(FPS)
