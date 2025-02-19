from settings import *
import pygame
import math
from LvL import load_lvl

class Player:
    def __init__(self):
        self.player_pos = Map().world__map()[1]
        self.collision_walls = Map().world__map()[2]
        self.end = Map().world__map()[3]
        self.x, self.y = self.player_pos
        self.angle = player_angle
        self.side = 50
        self.sensitivity = 0.004
        self.rect = pygame.Rect(*self.player_pos, self.side, self.side)
        self.num_lvl = 1
    
    @property
    def pos(self):
        return (self.x, self.y)

    def num_lvls(self):
        return self.num_lvl

    def collision(self, pos_x,  pos_y):
        next_rect = self.rect.copy()
        next_rect.move_ip(pos_x,  pos_y)
        hit_indexes = next_rect.collidelistall(self.collision_walls)
        
        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_walls[hit_index]
                if pos_x > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if pos_y > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                pos_x, pos_y = 0, 0
            elif delta_x > delta_y:
                pos_y = 0
            elif delta_y > delta_x:
                pos_x = 0

        collide_portal = next_rect.colliderect(self.end[0])
        
        if collide_portal:
            self.num_lvl += 1
            map = Map(self.num_lvl)
            self.player_pos = map.world__map()[1]
            self.collision_walls = map.world__map()[2]
            self.end = map.world__map()[3]
            self.x, self.y = self.player_pos[:]
            self.rect = pygame.Rect(*self.player_pos, self.side, self.side)
        
        self.x += pos_x
        self.y += pos_y      

    def movement(self):
        self.mouse_control()
        self.keys_control()
        self.rect.center = self.x, self.y
        self.angle = self.angle % (PI * 2)

    def keys_control(self):
        
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        self.player_speed_cos = player_speed * cos_a
        self.player_speed_sin = player_speed * sin_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            pos_x = self.player_speed_cos
            pos_y = self.player_speed_sin
            self.collision(pos_x, pos_y)
        if keys[pygame.K_s]:
            pos_x = -self.player_speed_cos
            pos_y = -self.player_speed_sin
            self.collision(pos_x, pos_y)
        if keys[pygame.K_a]:
            pos_x = self.player_speed_sin
            pos_y = -self.player_speed_cos
            self.collision(pos_x, pos_y)
        if keys[pygame.K_d]:
            pos_x = -self.player_speed_sin
            pos_y = self.player_speed_cos
            self.collision(pos_x, pos_y)
            
        
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    
    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensitivity


class Map:
    def __init__(self, num_lvl=1):
        self.player_pos, lvl = load_lvl(num_lvl)
        self.num_lvl = num_lvl
        self.world_map = {}
        self.collision_walls = []
        self.end = []
        text_map = lvl
        for j, row in enumerate(text_map):
            for i, char in enumerate(row):
                if char != '.':
                    if char == "#":
                        self.collision_walls.append(pygame.Rect(i * CELL, j * CELL, CELL, CELL))
                        self.world_map[(i * CELL, j * CELL)] = "#"
                    if char == "&":
                        self.end.append(pygame.Rect(i * CELL, j * CELL, CELL, CELL))
                        self.world_map[(i * CELL, j * CELL)] = "&"
    
    def world__map(self):
        return self.world_map, self.player_pos, self.collision_walls, self.end, self.num_lvl