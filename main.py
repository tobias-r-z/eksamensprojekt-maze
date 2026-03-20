#improtere pakker til python
import pygame
from pygame.locals import *
import random as rand
pygame.init()
#generer skærmen ti
screen=pygame.display.set_mode((300, 300))
white = [255, 255, 255]
screen.fill(white)
pygame.display.update()
#celle til labyrinten
class Cell:
    def __init__(self,x,y,scale):
        self.x=x
        self.y=y
        self.scale=scale
        #skal repræsentere hvor de forskellige vægge kan være.
        self.walls = [True,True,True,True] #venstre, højre, over, nedre
    #en metode som kan bygge væggen op omkring 
        self.start = False
        self.end = False
    def væggebyg(self):
        #ideen er at se om en af væggene er sande, og så tegne siderne
        if self.walls[0] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*100,self.y*100],[self.x*100,(self.y*100)+100])
        if self.walls[1] == True:
            pygame.draw.line(screen, [0,0,0], [(self.x*100)+100,self.y*100],[(self.x*100)+100,(self.y*100)+100])
        if self.walls[2] == True:
            pygame.draw.line(screen, [0,0,0], [(self.x*100)+100,self.y*100],[(self.x*100)+100,self.y*100])
        if self.walls[3] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*100,(self.y*100)+100],[(self.x*100)+100,(self.y*100)+100])
    
    def givekoords(self):
        return [self.x*100,self.y*100]
    def startslut(self,lab):
        if self.x==0 and self.y==0:
            self.start = True
        if self.x == len(lab)-1 and self.y == len(lab)-1:
            self.end = True


#laver labyrinten som et 2-dimensionelt array
labyrint2 =[[0, 1, 2], 
            [0, 1, 2], 
            [0, 1, 2]]
labvej =   [[0,0,0],
            [0,0,0],
            [0,0,0]]

def labbyg(lab):
    for y,row in enumerate(lab):
        for x,num in enumerate(row):
            cell = Cell(x,y,100)
            vej(cell)
            cell.væggebyg()
            cell.startslut(lab)
            #print(cell.start + cell.end)


            
def vej(acell):
    if acell.start == True:
        labvej[acell.y][acell.x] = 1
        rnd=rand.randint(0,1)
        if rnd == 0:
            acell.walls[1]=False
        if rnd == 1:
            acell.walls[3]=False

        
    if labvej[(acell.y)-1][(acell).x]==1 or labvej[(acell).y][(acell).x-1]==1:
        labvej[acell.y][acell.x] = 1
    #if acell.end == True:
       #labvej[acell.y][acell.x] = 1



running = True        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break        

    screen.fill([255,255,255])

    labbyg(labyrint2)

    pygame.display.update()

pygame.quit()