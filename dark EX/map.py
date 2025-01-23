from settings import *
import pygame
from LvL import *
text_map = lvl

world_map = set()
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '#':
            collision_walls.append(pygame.Rect(i * CELL, j * CELL, CELL, CELL))
            world_map.add((i * CELL, j * CELL))