import os
import random

from pygame import error
from pygame.base import get_error
from pygame.image import load

GAME_SRC_PATH = os.path.split(os.path.abspath(__file__))[0]
ASSETS_DIR = "assets"
SPRITES_DIR = os.path.join(GAME_SRC_PATH, f"{ASSETS_DIR}/sprites")
EXERCISES_DIR = os.path.join(GAME_SRC_PATH, f"{ASSETS_DIR}/exercises")


# functions to create resources
def load_sprite(sprite_name, with_alpha=True) -> tuple:
    full_path = os.path.join(SPRITES_DIR, sprite_name)

    try:
        loaded_sprite = load(full_path)
    except error:
        print("Cannot load image:", full_path)
        raise SystemExit(str(get_error()))

    if with_alpha:
        # image without transparent pixels
        return loaded_sprite.convert_alpha(), loaded_sprite.get_rect()
    else:
        return loaded_sprite.convert(), loaded_sprite.get_rect()


def load_code_blocks(exercise_file: str, section: str) -> str:
    full_path = os.path.join(EXERCISES_DIR, exercise_file)
    with open(full_path) as file_obj:  # <class '_io.TextIOWrapper'>
        text = file_obj.read()
    blocks = text.split("\n")

    block = random.choice(blocks)
    return block
