import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // CELL) * CELL, (b // CELL) * CELL


def ray_casting(screen, player_pos, player_angle, textures):
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
            x, dx = (xm + CELL, 1)    
        else:
            x, dx = (xm, -1)

        for i in range(0, WIDTH, CELL):
            depth_v = (x - ox) / cos_a
            y_v = oy + depth_v * sin_a
            if mapping(x + dx, y_v) in world_map:
                break
            x += dx * CELL

        # horizontals
        if sin_a >= 0:
            y, dy = (ym + CELL, 1)    
        else:
            y, dy = (ym, -1)

        for i in range(0, HEIGHT, CELL):
            depth_h = (y - oy) / sin_a
            x_h = ox + depth_h * cos_a
            if mapping(x_h, y + dy) in world_map:
                break
            y += dy * CELL

        # projection
        if depth_v < depth_h:
            depth, offset = (depth_v, y_v)
        else:
            depth, offset = (depth_h, x_h)
        
        offset = int(offset) % CELL
        depth = depth * math.cos(player_angle - cur_angle)
        if depth == 0:
            proj_height = min(int(PROJ_COEFF / 1), 2 * HEIGHT)
        else:
            proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
        

        # wall_texture = textures.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        # wall_texture = pygame.transform.scale(wall_texture, (SCALE, proj_height))
        # screen.blit(wall_texture, (ray * SCALE, HALF_HEIGHT - proj_height // 2))

        c = 255 / (1 + depth * depth * 0.00002)
        color = (c // 3, c // 2, c // 4)
        pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

        cur_angle += DELTA_ANGLE