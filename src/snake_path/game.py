"""
The structure of a Pygame program looks like this:
initialize_pygame()

while True:
    handle_input()
    process_game_logic()
    draw_game_elements()

`while` loop starts the game loop. Each iteration of this loop generates a single
frame of the game and usually performs the following operations:

1. Input handling: Input like pressed buttons, mouse motion, and VR controllers
position is gathered and then handled. Depending on the game, it can cause objects to
change their position, create new objects, request the end of the game, and so on.

2. Game logic: This is where most of the game mechanics are implemented. Here,
the rules of physics are applied, collisions are detected and handled, artificial
intelligence does its job, and so on. This part is also responsible for checking if
the player has won or lost the game.

3. Drawing: If the game hasn’t ended yet, then this is where the frame will be drawn
on screen. It will include all the items that are currently in the game and are
visible to the player.
"""

import sys

import pygame as pg

import settings
from helpers import load_sprite, load_code_blocks
from models import Snake

# Version check
if pg.get_sdl_version() < (2, 0, 0):
    sys.exit("This example requires pygame 2.")

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")


class SnakeTour:
    def __init__(self):
        self._init_pygame()
        self.screen = pg.display.set_mode((640, 426))
        self.background, _ = load_sprite("rain_stoppers_640.jpg", False)

        # Objects composition
        self.snake = Snake((400, 300))

        # Load and set the window logo
        self.logo, self.logo_rect = load_sprite("icons8-game-32.png", False)
        pg.display.set_icon(self.logo)

        # Font
        self.base_font = pg.font.SysFont("monospace", 32)

        self.clock = pg.time.Clock()

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        # Initialise Everything

        pg.init()
        pg.mixer.init()

        pg.display.set_caption("Space Rocks")
        pg.mouse.set_visible(True)

    def _handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        self.snake.move()

    def _draw(self):
        # fills the screen with a color
        # self.screen.fill((0, 0, 255))

        # To display one surface on another
        self.screen.blit(self.background, (0, 0))

        self.show_code_block()
        self.snake.draw(self.screen)

        pg.display.flip()

        self.clock.tick(settings.FPS)

    def show_code_block(self):
        # code string
        code_to_show = load_code_blocks("text.txt", "")
        # render/prepare text to be drawn
        text_surface = self.base_font.render(code_to_show, True, settings.WHITE)

        # coordinates to put text
        code_to_show_rect = pg.Rect(10, 10, 160, 40)
        # draw rectangular to put text in
        pg.draw.rect(self.screen, settings.BEIGE, code_to_show_rect, 2)

        self.screen.blit(text_surface, (code_to_show_rect.x, code_to_show_rect.y))
