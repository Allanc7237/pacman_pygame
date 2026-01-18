import pygame 
import sys
from constants import *
import os

class LevelNode(pygame.sprite.Sprite):
    def __init__(self,x,y,surface, type, rect=False, has_dot=False, neighbors=None, pressed = False):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        if type == "dot":
            self.has_dot = has_dot
        else:
            self.has_dot = False
        self.pressed  = pressed
        self.surface = surface
        self.position = pygame.Vector2(x,y)
        self.rect  = rect
        self.neighbors = neighbors

    def update(self, dt):
        pass
                
    def draw(self, screen):
        screen.blit(self.surface,self.position)

    def detect_collisions(self, mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_pos):
                if not self.pressed:
                    self.pressed = True
                    print(f"node at: {self.position}")
                    for n in self.neighbors:
                        print(f"Neighbor at :{n.position}")           

def generate_nodes(nodes):
    level_nodes = []
    current = os.getcwd()
    dot = os.path.join(current,DOT_IMAGE_PATH)
    jail = pygame.Surface((16,16))
    jail.set_alpha(0)
    surf = pygame.image.load(dot).convert_alpha()
    for node in nodes:
        temp_x = node[0]
        temp_y = node[1]  
        if node in JAIL_NODE_POS:
            new_node = LevelNode(temp_x,temp_y,jail,"jail")
        
        elif node == [SPAWN_X,SPAWN_Y]:
            new_node = LevelNode(temp_x,temp_y,jail,"spawn")
        
        elif node == [320, 320] or node == [304, 320]:
            new_node = LevelNode(temp_x,temp_y,jail,"gate")
        else:
            new_node = LevelNode(temp_x,temp_y,surf,"dot") 
        new_node.rect = pygame.Rect(temp_x,temp_y,17,17)
        level_nodes.append(new_node)
    return level_nodes 

def convert_path_to_nodes(path_text):
    path = []
    for item in path_text:
        if not item == "":
            temp = item.strip("[")
            text = temp.strip("]")
            nodes = text.split(",")
            temp_x = nodes[0]
            temp_y = nodes[1]
            x = int(temp_x)
            y = int(temp_y)
            path.append([x,y])
    return path



