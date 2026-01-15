import pygame 
import sys
from constants import *
import os

class LevelNode(pygame.sprite.Sprite):
    def __init__(self,x,y, surface, rect=None, pressed=False, has_dot=False, neighbors=None):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        pass
        self.position = pygame.Vector2(x,y)
        self.surface = surface
        self.rect  = rect
        self.neighbors = neighbors
        self.has_dot = has_dot
        self.pressed  = pressed


    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        pass

    def check_collisions(self,mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if(pygame.mouse.get_just_pressed()[0] and self.pressed == False):
                self.pressed = True
                
    def draw(self, screen):
        if not self.pressed:
            screen.blit(self.surface,self.position)     


def generate_nodes(width,height):
    nodes = []
    current = os.getcwd()
    dot = os.path.join(current,DOT_IMAGE_PATH)
    surf = pygame.image.load(dot).convert_alpha()
    temp_surf = pygame.Surface((12,12))
    temp_surf.fill("green")
    for i in range(0,width,16):
        for j in range(0,height,16):
            new_node = LevelNode(i,j,surf) 
            new_node.rect = pygame.Rect(i,j,16,16)
            nodes.append(new_node)     
    return nodes 

def generate_borders():
    pass



