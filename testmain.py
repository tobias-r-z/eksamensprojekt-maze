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
    
    def posvia(self,visited):

        rnddir = []

        directions = [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0)
        ]

        for dr, dy, dx in directions:
            nx, ny = self.x+dx, self.y+dy

            if nx>=0 and ny>=0 and not visited[ny][nx]:
                rnddir.append([[self.x,self.y],[nx,ny],dr])
        return rnddir
        





#laver labyrinten som et 2-dimensionelt array
def generate_rb():
    rows, cols = 12, 12
    grid = [[Cell(x, y, 50) for x in range(cols)] for y in range(rows)]

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
    rows, cols = 12, 12
    grid = [[Cell(x, y, 50) for x in range(cols)] for y in range(rows)]
    visited = [[False]*cols for _ in range(rows)]
    posvia=[]

    for i in range(rows*cols):
        if i == 0:
            posvia.append(grid[0][0].posvia(visited))
            visited[0][0] = True
        else:
            rand.shuffle(posvia)
            for t1 , s in enumerate(posvia):
                
                rand.shuffle(s)

                for t2, v in enumerate(s):
                    y = posvia[t1][t2][1][1]
                    x = posvia[t1][t2][1][0]
                    if visited[y][x] == True:
                        pass
                    else:
                        if posvia[t1][0][2] == "left":
                            grid[y][x].walls[1]=False
                            grid[y][x+1].walls[0]=False
                        elif posvia[t1][0][2] == "right":
                            grid[y][x].walls[0]=False
                            grid[y][x-1].walls[1]=False   
                        elif posvia[t1][0][2] == "up":
                            grid[y][x].walls[3]=False
                            grid[y+1][x].walls[2]=False   
                        elif posvia[t1][0][2] == "down":
                            grid[y][x].walls[3]=False
                            grid[y-1][x].walls[2]=False
    return grid


def labwhole(grid):
    
    for y,row in enumerate(grid):

        for x,col in enumerate(row):
            
            grid[y][x].væggebyg()

algo_input = input()

print("Du har valgt: " + algo_input)
if algo_input == "RB":
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