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
        #ideen  er at se om en af væggene er sande, og så tegne siderne
        if self.walls[0] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale,self.y*self.scale],[self.x*self.scale,(self.y*self.scale)+self.scale])
        if self.walls[1] == True:
            pygame.draw.line(screen, [0,0,0], [(self.x*self.scale)+self.scale,self.y*self.scale],[(self.x*self.scale)+self.scale,(self.y*self.scale)+self.scale])
        if self.walls[2] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale, self.y*self.scale], [(self.x*self.scale)+self.scale, self.y*self.scale])
        if self.walls[3] == True:
            pygame.draw.line(screen, [0,0,0], [self.x*self.scale,(self.y*self.scale)+self.scale],[(self.x*self.scale)+self.scale,(self.y*self.scale)+self.scale])
    
    #funktion der laver et array, som består af alle fie celler rundt om
    def posvia(self,visited):

        rnddir = [] 

        directions = [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0)
        ]

        for dr, dy, dx in directions: #beskriver 
            nx, ny = self.x+dx, self.y+dy #ny celles koordinator erklæres

            if cols > nx>=0 and rows > ny>=0 and not visited[ny][nx]: #mulige celler tjekkes
                rnddir.append([[self.x,self.y],[nx,ny],dr]) #nye koordinater lægges til
        return rnddir


#labyrint klasse for mere kompakt kode
class labyrint : 
    def __init__(self):

        #bygger et 2d array med objekter fra klassen Cell
        self.grid = [[Cell(x, y, celles) for x in range(cols)] for y in range(rows)]

        #bygger et 2d array med booleans.
        self.visited = [[False]*cols for _ in range(rows)]
    
    #funktion der kan fjerne væggene mellem 2 celler
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
    lab = labyrint()

    def dfs(r, c): #lokal funktion

        lab.visited[r][c] = True #celle markeres som besøgt

        directions = [
            ("left", 0, -1),
            ("right", 0, 1),
            ("up", -1, 0),
            ("down", 1, 0)
        ]

        rand.shuffle(directions) #en tilfældig retning udvælges

        for dir, dr, dc in directions:
            nr, nc = r + dr, c + dc #ny celles koordinator erklæres

            if 0 <= nr < rows and 0 <= nc < cols and not lab.visited[nr][nc]:

                # fjern vægge mellem celler
                lab.remove_walls(c,r,nc,nr,dir)
                
                dfs(nr, nc) #rekurtere ny koordinator

    dfs(0, 0)
    return lab.grid

def generate_prim():

    lab = labyrint()
    frontier = [] #arrayet som skal holde de mulige 

    lab.visited[0][0] = True #celle markeres som besøgt

    frontier.extend(lab.grid[0][0].posvia(lab.visited)) #array forlænges med posvia funktion

    while frontier: #frontier > 0

        rand.shuffle(frontier) #tilfædig celle udvælges

        (x1,y1),(x2,y2),direction = frontier.pop() #celle erklæres ved de forskellige funktioner

        if not lab.visited[y2][x2]: #er en celle ikke besøgt
            lab.remove_walls(x1,y1,x2,y2,direction) 

            lab.visited[y2][x2] = True #den ny celle skal nu være besøgt
            frontier.extend(lab.grid[y2][x2].posvia(lab.visited)) #nye mulige celler tilføjes

    return lab.grid

#funktion der bygger labyrinten ud fra en gitterstruktur.
def labwhole(grid):
    
    for y,row in enumerate(grid):

        for x,col in enumerate(row):
            
            grid[y][x].væggebyg() #væg bygges

#de forskellige inputs
algo_input = input("Hvilken algoritme skal bruges? ")
cols = int(input("Hvor bred skal labyrinten være? "))
rows = int(input("Hvor høj skal labyrinten være? "))
celles = int(input("hvor store skal cellerne være (kvadrat)? "))

pygame.init()

#generer skærmen i forhold til input
screen=pygame.display.set_mode((cols*celles, rows*celles))

white = [255, 255, 255]

screen.fill(white)

pygame.display.update()

#generering af recursive backtracking algoritme
if algo_input.lower() == "rb":
    maze1 = generate_rb()

#generering af prim algoritme
if algo_input == "prim":
    maze1 = generate_prim()

#loop der gennem går hvert frame
running = True        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break        

    screen.fill([255,255,255]) #skærm bygges

    labwhole(maze1) #labyrintgitter bygges

    pygame.display.update()

pygame.quit()