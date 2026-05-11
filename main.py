#improtere pakker til python
import pygame
from pygame.locals import *
import random as rand
pygame.init()
#generer skærmen ti
screen=pygame.display.set_mode((600, 600))
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
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale,self.y*self.scale],[self.x*self.scale,(self.y*self.scale)+self.scale])
        if self.walls[1] == True:
            pygame.draw.line(screen, [0,0,0], [(self.x*self.scale)+self.scale,self.y*self.scale],[(self.x*self.scale)+self.scale,(self.y*self.scale)+self.scale])
        if self.walls[2] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale, self.y*self.scale], [(self.x*self.scale)+self.scale, self.y*self.scale])
        if self.walls[3] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale,(self.y*self.scale)+self.scale],[(self.x*self.scale)+self.scale,(self.y*self.scale)+self.scale])
    
    def givekoords(self):
        return [self.x*100,self.y*100]
    def startslut(self,lab):
        if self.x==0 and self.y==0:
            self.start = True
        if self.x == len(lab)-1 and self.y == len(lab)-1:
            self.end = True


#laver labyrinten som et 2-dimensionelt array

grid = [[0 for _ in range(6)] for _ in range(6)]

def newway():
    rows, cols = 6, 6

# lav tom grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
# start position
    r, c = 0, 0
    grid[r][c] in [2,3]  # start på path

    #while løkke bruges til at gentage path building
    while r < rows - 1 or c < cols - 1:
        moves = []

    # må gå ned
        if r < rows - 1:
            moves.append("down")

    # må gå højre
        if c < cols - 1:
            moves.append("right")

        #en tilfældig retning vælges
        move = rand.choice(moves)
        #den retning bliver lagt til positionen
        if move == "down":
            r += 1
        else:
            c += 1

        grid[r][c] = 2  # markér path
    return grid

def opbygning(cell,grid,x,y):
    rows = (len(grid))
    cols = (len(grid[0]))
    current = grid[y][x]

    # venstre
    if x > 0 and grid[y][x-1] == current:
        cell.walls[0] = False

    # højre
    if x < cols-1 and grid[y][x+1] == current:
        cell.walls[1] = False

    # op
    if y > 0 and grid[y-1][x] == current:
        cell.walls[2] = False

    # ned
    if y < rows-1 and grid[y+1][x] == current:
        cell.walls[3] = False   
         #print(cell.walls)

newgrid = newway()


def labwhole(grid):
    for y,row in enumerate(grid):

        for x,col in enumerate(row):
            

            newcell = Cell(x,y,100)

            if col in [2,3]:
                opbygning(newcell,grid,x,y)
            newcell.væggebyg()
            print(grid)

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