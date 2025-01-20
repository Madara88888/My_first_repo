import math
# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
fps = 90
cell_size = 100

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = HEIGHT
DELTA_ANGLE = FOV / NUM_RAYS
DIST = 2.6 * NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * cell_size
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

# colors
count = 1
r, g, b = 10, 10, 100
WHITE = (255, 255, 255)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
PURPLE = (120, 0, 120)

