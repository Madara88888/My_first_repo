import pygame
from settings import *
from player import Player
from map import world_map, collision_walls
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.K_LSHIFT:
            scene = 1
                

    player.movement()
    screen.fill((0, 0, 0))

    drawing.background()
    drawing.world(player.pos, player.angle)

    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(str(round(((pygame.time.get_ticks()) / 1000), 1)) + " секунд" + f"  {round(clock.get_fps(), 2)} FPS")

        