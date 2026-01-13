import pygame 
import sys
from constants import *
import os

class LevelNode:
    def __init__(self, position, surface, neighbors=None):
        self.position = position
        self.surface = surface
        self.neighbors = neighbors

class WallNode(LevelNode):
    def __init__(self,position,surface):
        super().__init__(position,surface)


def generate_nodes(width,height):
    nodes = []
    for i in range(0,width,16):
        for j in range(0,height,16):
            nodes.append((i+8,j+8))     
    return nodes 

def generate_borders():
    pass



