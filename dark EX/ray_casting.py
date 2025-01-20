import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // cell_size) * cell_size, (b // cell_size) * cell_size


def ray_casting(screen, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        if sin_a:
            sin_a = sin_a
        else:
            sin_a = 0.000001
        if cos_a:
            cos_a = cos_a
        else:
            cos_a = 0.000001

        # verticals
        if cos_a >= 0:
            x, dx = (xm + cell_size, 1)    
        else:
            x, dx = (xm, -1)

        for i in range(0, WIDTH, cell_size):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * cell_size

        # horizontals
        if sin_a >= 0:
            y, dy = (ym + cell_size, 1)    
        else:
            y, dy = (ym, -1)

        for i in range(0, HEIGHT, cell_size):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * cell_size

        # projection
        if depth_v < depth_h:
            depth = depth_v
        else:
            depth = depth_h
        depth = depth * math.cos(player_angle - cur_angle)
        if depth == 0:
            proj_height = min(int(PROJ_COEFF / 1), 2 * HEIGHT)
        else:
            proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
        c = 255 / (1 + depth * depth * 0.0001)
        color = (c// 2, c , c // 3)
        pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE