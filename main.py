#improtere pakker til python
import pygame
import random
from pygame.locals import *
pygame.init()
#generer skærmen ti
screen=pygame.display.set_mode(800, 800)

class Cell:
    def __init__(self,x,y):
        self.x
        self.y
        self.walls = [True,True,True,True] #venstre, højre, over, nedre
        self.visited = False
