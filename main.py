#improtere pakker til python
import pygame
import random
from pygame.locals import *
pygame.init()
#generer skærmen ti
screen=pygame.display.set_mode((300, 300))
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
    #en metode som kan bygge væggen op omkring 
    def væggebyg(self):
        #ideen er at se om en af væggene er sande, og så tegne siderne
        if self.walls[1] == True:
            pygame.draw.line(screen, [0,0,0], [self.x+50,self.y+50],[self.x+50,self.y-50])
    def tegn(self):
        pygame.draw.rect(screen,[0,0,200],[100, 100, 400, 100],2)        


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

labyrint2 = [[1, 2, 3], 
             [1, 2, 3], 
             [1, 2, 3]]

def labbyg(lab):
    for row in lab:
        for num in row:
            cell = Cell(num,lab.index(row))
            cell.væggebyg()

def labyrintalgo():
    for row in labyrint:
        for x in row:
            #print(labyrint.index(row),row.index(x))
            x.væggebyg()
            x.tegn()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break        

    screen.fill([255,255,255])

    labyrintalgo()

    #pygame.draw.line(screen, [0,0,0], [75,75],[100,100])

    pygame.display.update()



pygame.quit()