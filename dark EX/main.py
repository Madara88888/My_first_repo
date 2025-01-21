import pygame
from settings import *
from player import Player
import math
from map import world_map
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




    
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(str(round(((pygame.time.get_ticks()) / 1000), 1)) + " секунд" + f"  {round(clock.get_fps(), 2)} FPS")

        