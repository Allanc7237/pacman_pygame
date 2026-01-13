import pygame 
import sys
from constants import *

class LevelNode:
    def __init__(self, neighbors, position, surface):
        self.neighbors = neighbors
        self.position = position
        self.surface = surface

class WallNode(LevelNode):
    def __init__(self,position,surface):
        super.__init__(position,surface)


def generate_nodes(width,height):
    nodes = []
    for i in range(0,width,26):
        for j in range(0,height,34):
            nodes.append((i,j))
    return nodes

def generate_borders():
    pass



