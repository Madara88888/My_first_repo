import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 90
CELL = 100
QUANTITY_LVLS = 5
size_lvl = 6

# texture settings
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // CELL


# ray casting settings
PI = math.pi
FOV = PI / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = HEIGHT
DELTA_ANGLE = FOV / NUM_RAYS
DIST = 2.6 * NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * CELL
SCALE = WIDTH // NUM_RAYS


# player settings
RAD = 12
player_angle = 0
player_speed = 3.3


