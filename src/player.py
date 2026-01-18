from character_node import Character_Node

class Player_Node(Character_Node):
    def __init__(self, spawn_vector, image_path, current_node=None, next_node=None, previous_node=None):
        super().__init__(spawn_vector, image_path)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
    def update(self,dt):
        pass