import pygame
import sys
from constants import *
from level_generator import generate_nodes, LevelNode, convert_path_to_nodes
from player import Player_Node
import os

def set_neighbors(nodes):
    for node in nodes:
        neighbor_list = [None,None,None,None]
        temp_neighbors = []
        x1 = node.position[0]
        y1 = node.position[1]
        temp_neighbors = node.rect.collideobjectsall(nodes)
        for n in temp_neighbors:

            if node.position == n:
                continue

            x2 = n.position[0]
            y2 = n.position[1]

            if x1 == x2:
                if y1 > y2:
                    neighbor_list[0] = n
                else:
                    neighbor_list[2] = n
            else:
                if x1 > x2:
                    neighbor_list[3] = n
                else:
                    neighbor_list[1] = n
        node.neighbors = neighbor_list


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pycman")
game_clock = pygame.time.Clock()

current_directory = os.getcwd()
bg_directory = os.path.join(current_directory, BG_IMAGE_PATH)
font_directory = os.path.join(current_directory, FONT_PATH)
player_directory = os.path.join(current_directory, PLAYER_PATH)
node_path = os.path.join(current_directory, "content/node_position.txt")

test_font = pygame.font.Font(font_directory, 50)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
dots = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
players = pygame.sprite.Group()

LevelNode.containers = (updatable,drawable,dots)
Player_Node.containers = (updatable,drawable,players)

level_bg = pygame.image.load(bg_directory).convert()

with open(node_path, "r") as f:
    content = f.read()
    nodes_text = content.split("\n")

node_pos = convert_path_to_nodes(nodes_text)

test_nodes = generate_nodes(node_pos)
set_neighbors(test_nodes)
player1 = Player_Node(pygame.Vector2(SPAWN_X,SPAWN_Y),player_directory)
player1.starting_node = player1.rect.collideobjects(test_nodes)
for node in test_nodes:
    if node.position == player1.position:
        player1.starting_node = node
        player1.previous_node = node
        player1.next_node = node.neighbors[1]
        break
print(player1.starting_node.position)
screen.fill("white")

def main():
    try:
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.blit(level_bg, (0,0))

            for item in drawable:
                item.draw(screen)

            for item in dots:
                item.detect_collisions(mouse_pos) 

            pygame.display.update()
            dt = game_clock.tick(60)/1000
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
