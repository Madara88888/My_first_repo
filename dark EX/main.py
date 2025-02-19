import pygame
from settings import *
from player import Player
from drawing import Drawing
from LvL import load_lvl
from ray_casting import ray_casting

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)
pygame.mouse.set_visible(False)

scene = 0
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    scene = player.num_lvl
    if scene < QUANTITY_LVLS - 1:
        player.movement()
        screen.fill((0, 0, 0))

        drawing.background()
        drawing.world(player.pos, player.angle, player.num_lvls())
    if scene == QUANTITY_LVLS - 1:
        drawing.END()
        if t == 0:
            print(drawing.END())
            t = 1
    pygame.display.flip()
    clock.tick(FPS)
    Time = drawing.END()
    pygame.display.set_caption(Time + " секунд" + f"  {round(clock.get_fps(), 2)} FPS")

        