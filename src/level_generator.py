import pygame 
import sys
from constants import *
import os

class LevelNode:
    def __init__(self, position, surface, rect, pressed=False, has_dot=False, neighbors=None):
        self.position = position
        self.surface = surface
        self.rect  = rect
        self.neighbors = neighbors
        self.has_dot = has_dot
        self.pressed  = pressed

def generate_nodes(width,height):
    nodes = []
    surf = pygame.image.load(DOT_IMAGE_PATH)
    temp_surf = pygame.Surface((12,12))
    temp_surf.fill("green")
    temp_surf.set_alpha(100)
    for i in range(0,width,16):
        for j in range(0,height,16):
            new_node = LevelNode((i,j),temp_surf,None) 
            new_node.rect = pygame.Rect(i,j,16,16)
            nodes.append(new_node)     
    return nodes 

def generate_borders():
    pass



