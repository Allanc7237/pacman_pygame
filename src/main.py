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
level_ui_left = pygame.Surface((427,720))
level_ui_right = pygame.Surface((427,720))
level_ui_left.fill("green")
level_ui_right.fill("red")
game_clock = pygame.time.Clock()
area = width * height
test_nodes = generate_nodes(560,720)
screen.fill("white")
def main():
    try:
        print(f"{len(test_nodes)} nodes created")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.blit(level_bg, (427,0))
            screen.blit(level_ui_left, (0,0))
            screen.blit(level_ui_right, (887,0))
            for node in test_nodes:
                pygame.draw.circle(level_bg, "white",node,2)
            pygame.display.update()
            dt = game_clock.tick(60)/1000
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
