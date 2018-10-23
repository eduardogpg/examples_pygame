import pygame
import sys

pygame.init()

WIDTH = 400
HEIGHT = 500

#RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Rectangulos!')

rectangle = pygame.Rect(150, 10, 80, 100)

print(rectangle.x)
print(rectangle.y)

rectangle.center = ( WIDTH / 2, HEIGHT / 2 )

print(rectangle.x)
print(rectangle.y)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill(WHITE)

    #Existen dos formas de representar a un rectangulo, por una tupla o un objeto.
    pygame.draw.rect(display, GREEN, (10, 10, 80, 100) )
    pygame.draw.rect(display, BLUE, rectangle)

    pygame.display.update()
