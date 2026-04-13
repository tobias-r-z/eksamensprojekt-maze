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

grid = [[0 for _ in range(3)] for _ in range(3)]

def newway():
    rows, cols = 3, 3

# lav tom grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

# start position
    r, c = 0, 0
    grid[r][c] = 2  # start på path

    while r < rows - 1 or c < cols - 1:
        moves = []

    # må gå ned
        if r < rows - 1:
            moves.append("down")

    # må gå højre
        if c < cols - 1:
            moves.append("right")

        move = rand.choice(moves)

        if move == "down":
            r += 1
        else:
            c += 1

        grid[r][c] = 2  # markér path
    return grid

def opbygning(cell,waygrid,row,col,x,y):

    if col == 2 and cell.end == True:
        cell.walls [rand.choice([1,3])] = False

        if waygrid[y-1][x] == 2 and cell.start == False:
            cell.walls[2] = False

        if row[x-1] == 2 and cell.start == False:
            cell.walls[0] = False

    elif cell.end:

        if waygrid[y-1][x] == 2 and cell.start == True:
                    cell.walls[2] = False

        if row[x-1] == 2 and cell.start == True:
                    cell.walls[0] = False

newgrid = newway()

def labwhole(grid):
    for y,row in enumerate(grid):

        for x,col in enumerate(row):
            
            newcell = Cell(x,y,100)
            opbygning(newcell,grid,row,col,x,y)
            newcell.væggebyg()



"""def labbyg(labvej):
    for y,row in enumerate(labvej):
        yrow = []
        for x,num in enumerate(row):
            newcell=Cell(x,y,100)
            yrow.append(newcell)
        labvej[y]=yrow
"""
"""def labway(labvej):
        for y,row in enumerate(labvej):

            for x,num in enumerate(row):
                if num.x-1 == 0 and num.y-1 == 0:
                    num.start = True    
                elif num.x-1 == 2 and num.y-1 == 2:
                    num.end = True
                if num.end == True:
                    break
                if 
"""




            
"""def vej(acell):
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
"""


running = True        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break        

    screen.fill([255,255,255])

    labwhole(newgrid)

    pygame.display.update()

pygame.quit()