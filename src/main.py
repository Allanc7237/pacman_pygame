import pygame
import sys
from constants import *
from level_generator import generate_nodes, LevelNode
import os

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pycman")
game_clock = pygame.time.Clock()

current_directory = os.getcwd()
bg_directory = os.path.join(current_directory, BG_IMAGE_PATH)
font_directory = os.path.join(current_directory, FONT_PATH)

test_font = pygame.font.Font(font_directory, 50)

save_surf = test_font.render("Click to Save",False,"black")
save_rect = save_surf.get_rect(center =(SCREEN_WIDTH*.75,SCREEN_HEIGHT/2) )

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
dots = pygame.sprite.Group()
ghosts = pygame.sprite.Group()

LevelNode.containers = (updatable,drawable,dots)

temp = pygame.image.load(bg_directory)

level_bg =  temp.convert()

test_nodes = generate_nodes(int(SCREEN_WIDTH/2),720)
screen.fill("white")

def main():
    try:
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.blit(level_bg, (0,0))
            pygame.draw.rect(screen,"pink",save_rect,2,10)
            screen.blit(save_surf,save_rect)

            for item in drawable:
                item.draw(screen) 

            for item in updatable:    
                item.check_collisions(mouse_pos)

            pygame.display.flip()
            dt = game_clock.tick(60)/1000
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
