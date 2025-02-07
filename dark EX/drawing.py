import pygame
from settings import *
from ray_casting import ray_casting
# from map import mini_map

class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.texture = {"#": pygame.image.load("img/1.png").convert(), "&": pygame.image.load("img/2.png").convert()}
        self.overlay = pygame.image.load("img/overlay.png").convert()
        self.r, self.g, self.b = 10, 10, 100
        self.count = 1
        
    def background(self):
        pygame.draw.rect(self.screen, (self.r, self.g, self.b), (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, (40, 40, 40), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        
        if (pygame.time.get_ticks()) % 1000 <= 10:
            if self.count == 1:
                self.r += 1
                self.g += 1
                self.b += 2
                if self.b >= 250:
                    self.count = 0
            elif self.count == 0:
                self.r -= 1
                self.g -= 1
                self.b -= 2
                if self.b <= 100:
                    self.count = 1

    def world(self, player_pos, player_angle, num_lvl):
        ray_casting(self.screen, player_pos, player_angle, self.texture, self.overlay, num_lvl)
