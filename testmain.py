#improtere pakker til python
import pygame
from pygame.locals import *
import random as rand



#celle til labyrinten
class Cell:

    def __init__(self,x,y,scale):
        self.x=x
        self.y=y
        self.scale=scale
        #skal repræsentere hvor de forskellige vægge kan være.
        self.walls = [True,True,True,True] #venstre, højre, over, nedre

    #en metode som kan bygge væggen op omkring 
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
    
    def posvia(self,visited):
        #rows, cols = 24, 24
        rnddir = []

        directions = [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0)
        ]

        for dr, dy, dx in directions:
            nx, ny = self.x+dx, self.y+dy

            if cols > nx>=0 and rows > ny>=0 and not visited[ny][nx]:
                rnddir.append([[self.x,self.y],[nx,ny],dr])
        return rnddir

class labyrint : 
    def __init__(self):
        self.row = rows
        self.col = cols
        self.grid = [[Cell(x, y, 25) for x in range(cols)] for y in range(rows)]
        
    

def remove_walls(x1 ,y1 ,x2 ,y2 , dir:str, grid):
    if dir == "left":
        grid[y1][x1].walls[0] = False
        grid[y2][x2].walls[1] = False
    elif dir == "right":
        grid[y1][x1].walls[1] = False
        grid[y2][x2].walls[0] = False
    elif dir == "up":
        grid[y1][x1].walls[2] = False
        grid[y2][x2].walls[3] = False
    elif dir == "down":
        grid[y1][x1].walls[3] = False
        grid[y2][x2].walls[2] = False





#laver labyrinten som et 2-dimensionelt array
def generate_rb():
    #rows, cols = 24, 24
    grid = [[Cell(x, y, 25) for x in range(cols)] for y in range(rows)]

    visited = [[False]*cols for _ in range(rows)]

    def dfs(r, c):
        visited[r][c] = True

        directions = [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0)
        ]

        rand.shuffle(directions)

        for dir, dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:

                # fjern vægge mellem celler
                if dir == "left":
                    grid[r][c].walls[0] = False
                    grid[nr][nc].walls[1] = False
                elif dir == "right":
                    grid[r][c].walls[1] = False
                    grid[nr][nc].walls[0] = False
                elif dir == "up":
                    grid[r][c].walls[2] = False
                    grid[nr][nc].walls[3] = False
                elif dir == "down":
                    grid[r][c].walls[3] = False
                    grid[nr][nc].walls[2] = False

                dfs(nr, nc)

    dfs(0, 0)
    return grid

def generate_prim():
    #rows, cols = 24, 24
    grid = [[Cell(x, y, 25) for x in range(cols)] for y in range(rows)]
    visited = [[False]*cols for _ in range(rows)]

    frontier = []

    visited[0][0] = True
    frontier.extend(grid[0][0].posvia(visited))

    while frontier:
        rand.shuffle(frontier)
        (x1,y1),(x2,y2),direction = frontier.pop()

        if not visited[y2][x2]:
            remove_walls(x1,y1,x2,y2,direction,grid)

            visited[y2][x2] = True
            frontier.extend(grid[y2][x2].posvia(visited))

    return grid

def labwhole(grid):
    
    for y,row in enumerate(grid):

        for x,col in enumerate(row):
            
            grid[y][x].væggebyg()

algo_input = input("Hvilken algoritme skal bruges? ")
cols = int(input("Hvor bred skal labyrinten være? "))
rows = int(input("Hvor høj skal labyrinten være? "))
celler = int(input("hvor store skal cellerne være (kvadrat)? "))

pygame.init()

#generer skærmen ti
screen=pygame.display.set_mode((cols*25, rows*25))

white = [255, 255, 255]

screen.fill(white)

pygame.display.update()

if algo_input == "RB" or "rb":
    maze1 = generate_rb()
if algo_input == "prim":
    maze1 = generate_prim()

running = True        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break        

    screen.fill([255,255,255])

    labwhole(maze1)

    pygame.display.update()

pygame.quit()