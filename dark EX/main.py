import pygame
from settings import *
from player import Player
import math
from map import world_map, collision_walls
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill((0, 0, 0))

    drawing.background()
    drawing.world(player.pos, player.angle)

    # pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12) 
    # for x,y in world_map:
    #     pygame.draw.rect(screen, (255, 0, 0), (x, y, CELL, CELL), 2)

    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(str(round(((pygame.time.get_ticks()) / 1000), 1)) + " секунд" + f"  {round(clock.get_fps(), 2)} FPS")

        