import pygame
import sys
from constants import *
from level_generator import generate_nodes
import os

current_directory = os.getcwd()
bg_directory = os.path.join(current_directory, BG_IMAGE_PATH)
print(bg_directory)
pygame.init()
width = SCREEN_WIDTH
height = SCREEN_HEIGHT
screen = pygame.display.set_mode((width,height))
level_bg =  pygame.image.load(bg_directory)
level_ui = pygame.Surface((640,720))
level_ui.fill("black")
game_clock = pygame.time.Clock()
area = width * height
test_nodes = generate_nodes(640,720)
screen.fill("white")
def main():
    try:
        #print(f"{len(test_nodes)} nodes created")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(level_bg, (0,0))
            screen.blit(level_ui, (640,0))
            for node in test_nodes:
                pygame.draw.circle(level_bg,"white",node,2)
            pygame.display.update()
            dt = game_clock.tick(60)/1000
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
