from character_node import Character_Node

class Ghost_Node(Character_Node):
    def __init__(self, name, image_path, current_node=None, next_node=None, previous_node=None):
        super().__init__(spawn_vector, image_path)
            match name:
                case "inky":
                    pass
                case "blinky":
                    pass
                case "clyde"
                    pass
                case "pinky"


    def draw(self,screen):
        screen.blit(self.image,self.rect)
            
    def update(self,dt):
        pass