from pygame.math import Vector2


# Game Options and Settings
TITLE = "Type-speed and learn Python"
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 10

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# Movement (x, y)
UP_MOVE = Vector2(0, -1)
DOWN_MOVE = Vector2(0, 1)
LEFT_MOVE = Vector2(-1, 0)
RIGHT_MOVE = Vector2(-1, 0)

# Define Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BEIGE = (245, 245, 220, 255)
BURLYWOOD = (222, 184, 135, 255)
BLUEVIOLET = (138, 43, 226, 255)

# Block Settings
BLOCK_WIDTH = 23
BLOCK_HEIGHT = 15
