import pygame
from settings import *
from ray_casting import ray_casting
# from map import mini_map

class Drawing:
    def __init__(self, screen):
        self.screen = screen

    def background(self):
        pygame.draw.rect(self.screen, (r, g, b), (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, (40, 40, 40), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle)
