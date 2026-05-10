#improtere pakker til python
import pygame
#from pygame.locals import *
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
        #ideen  er at se om en af væggene er sande, og så tegne siderne
        if self.walls[0] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale,self.y*self.scale],[self.x*self.scale,(self.y*self.scale)+self.scale])
        if self.walls[1] == True:
            pygame.draw.line(screen, [0,0,0], [(self.x*self.scale)+self.scale,self.y*self.scale],[(self.x*self.scale)+self.scale,(self.y*self.scale)+self.scale])
        if self.walls[2] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale, self.y*self.scale], [(self.x*self.scale)+self.scale, self.y*self.scale])
        if self.walls[3] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale,(self.y*self.scale)+self.scale],[(self.x*self.scale)+self.scale,(self.y*self.scale)+self.scale])
    
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


#labyrint klasse for mere kompakt kode
class labyrint : 
    def __init__(self):
        self.grid = [[Cell(x, y, celles) for x in range(cols)] for y in range(rows)]
        self.visited = [[False]*cols for _ in range(rows)]
    
    def remove_walls(self,x1 ,y1 ,x2 ,y2 , dir:str):
        grid = self.grid
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
    lab = labyrint()

    def dfs(r, c):

        lab.visited[r][c] = True

        directions = [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0)
        ]

        rand.shuffle(directions)

        for dir, dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and not lab.visited[nr][nc]:

                # fjern vægge mellem celler
                lab.remove_walls(c,r,nc,nr,dir)
                
                dfs(nr, nc)

    dfs(0, 0)
    return lab.grid

def generate_prim():
    #rows, cols = 24, 24
    lab = labyrint()
    frontier = []

    lab.visited[0][0] = True
    frontier.extend(lab.grid[0][0].posvia(lab.visited))

    while frontier:
        rand.shuffle(frontier)
        (x1,y1),(x2,y2),direction = frontier.pop()

        if not lab.visited[y2][x2]:
            lab.remove_walls(x1,y1,x2,y2,direction)

            lab.visited[y2][x2] = True
            frontier.extend(lab.grid[y2][x2].posvia(lab.visited))

    return lab.grid

def labwhole(grid):
    
    for y,row in enumerate(grid):

        for x,col in enumerate(row):
            
            grid[y][x].væggebyg()

algo_input = input("Hvilken algoritme skal bruges? ")
cols = int(input("Hvor bred skal labyrinten være? "))
rows = int(input("Hvor høj skal labyrinten være? "))
celles = int(input("hvor store skal cellerne være (kvadrat)? "))

pygame.init()

#generer skærmen ti
screen=pygame.display.set_mode((cols*celles, rows*celles))

white = [255, 255, 255]

screen.fill(white)

pygame.display.update()

if algo_input.lower() == "rb":
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