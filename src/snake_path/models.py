import random

import pygame as pg
from pygame.math import Vector2
import settings

# from settings import SCREEN_HEIGHT, SCREEN_WIDTH, UP_MOVE, DOWN_MOVE, LEFT_MOVE, RIGHT_MOVE


from helpers import load_sprite


class GameObject:
    def __init__(self, position, sprite, velocity):
        self.start_position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.start_position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.start_position = self.start_position + self.velocity

    def collides_with(self, other_obj):
        distance = self.start_position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius


class Snake(GameObject):
    # MANEUVERABILITY = 3

    def __init__(self, position):
        self.direction = Vector2(settings.UP_MOVE)
        super().__init__(position, load_sprite("python_snake.png")[0], Vector2(0))

        self.length = 1
        self.positions = [(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)]
        # self.direction = random.choice([settings.UP_MOVE, settings.DOWN_MOVE,
        #                                 settings.LEFT_MOVE,
        #                                 settings.RIGHT_MOVE])
        self.color = (0, 0, 255)  # RGB code for blue
        self.score = settings.BLUEVIOLET

    # def draw(self):
    #     ...

    def handle_keys(self):
        pass


class Food:
    def randomize_position(self):
        pass

    def draw(self):
        pass
