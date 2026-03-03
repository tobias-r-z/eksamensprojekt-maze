import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("labyrint simulator")

colour1 = (255,0,0)
colour2 = (0,255,0)
rectangel = [40, 40, 100, 100]
screen.fill(colour1)
pygame.display.flip()
pygame.draw.rect(screen,colour2,rectangel,0)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
