import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(screen, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        if cos_a >= 0:
            x, dx = (xm + TILE, 1)    
        else:
            x, dx = (xm, -1)

        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # horizontals
        if sin_a >= 0:
            y, dy = (ym + TILE, 1)    
        else:
            y, dy = (ym, -1)

        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        # projection
        if depth_v < depth_h:
            depth = depth_v
        else:
            depth = depth_h
        depth = depth * math.cos(player_angle - cur_angle)
        if depth == 0:
            proj_height = PROJ_COEFF / 1
        else:
            proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.0001)
        color = (c// 2, c , c // 3)
        pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE