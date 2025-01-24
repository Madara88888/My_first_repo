from settings import *
import pygame
import math
from map import collision_walls
from LvL import *

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.side = 50
        self.sensitivity = 0.004
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
    
    @property
    def pos(self):
        return (self.x, self.y)

    def collision(self, pos_x,  pos_y):
        next_rect = self.rect.copy()
        next_rect.move_ip( pos_x,  pos_y)
        hit_indexes = next_rect.collidelistall(collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
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
        self.x += pos_x
        self.y += pos_y

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle = self.angle % (PI * 2)

    def keys_control(self):
        fow_change = 0
        self.rect.center = self.x, self.y

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