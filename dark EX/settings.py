import math
# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 90
CELL = 100
size_lvl = 40

# texture settings
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // CELL


# ray casting settings
FOV = math.pi / 3
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
player_speed = 2

# colors
WHITE = (255, 255, 255)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
PURPLE = (120, 0, 120)

