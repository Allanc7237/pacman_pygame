import pygame 
import sys
from constants import *
import os

class LevelNode:
    def __init__(self, position, surface, rect, has_dot=False, neighbors=None):
        self.position = position
        self.surface = surface
        self.neighbors = neighbors
        self.has_dot = has_dot
        self.rect  = rect

def generate_nodes(width,height):
    nodes = []
    surf = pygame.image.load(DOT_IMAGE_PATH)
    for i in range(0,width,16):
        for j in range(0,height,16):
            new_node = LevelNode((i,j),surf,None) 
            new_node.rect = pygame.Rect(0,0,16,16)
            nodes.append(new_node)     
    return nodes 

def generate_borders():
    pass



