#improtere pakker til python
import pygame
import random
from pygame.locals import *
pygame.init()
#generer skærmen ti
screen=pygame.display.set_mode((600, 600))
white = [255, 255, 255]
screen.fill(white)
pygame.display.update()
#celle til labyrinten
class Cell:
    def __init__(self,x,y):
        self.x=x+1*150
        self.y=y+1*150
        #skal repræsentere hvor de forskellige vægge kan være.
        self.walls = [True,True,True,True] #venstre, højre, over, nedre
        self.visited = False
    def væggebyg(self):
        if self.walls[1] == True:
            pygame.draw.line(screen, [0,0,0], [self.x+150,self.y+150],[self.x+150,self.y-150])



#definerer hver celle
cell00 = Cell(0,0)
cell01 = Cell(1,0)
cell02 = Cell(2,0)
cell10 = Cell(0,1)
cell11 = Cell(1,1)
cell12 = Cell(2,1)
cell20 = Cell(0,2)
cell21 = Cell(1,2)
cell22 = Cell(2,2)

#laver labyrinten som et 2-dimensionelt array
labyrint = [[cell00, cell01, cell02],
            [cell10, cell11, cell12],
            [cell20, cell21, cell22]]


def labyrintalgo():
    for row in labyrint:
        for x in row:
            x.væggebyg()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()