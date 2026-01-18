import pygame
import os

class Character_Node(pygame.sprite.Sprite):
    def __init__(self, spawn_vector, image_path, current_node=None,next_node=None,previous_node=None):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = spawn_vector
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self,screen):
        pass
    
    def update(self,dt):
        pass
