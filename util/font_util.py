import sys

import os

sys.path.append(os.path.realpath('..'))

import random
from PIL import ImageFont

from config.image_config import font_dir
from config.image_config import chs_font
from config.image_config import en_font


def get_font_fullpaths(kind):
    path = None
    if kind == chs_font:
        path = os.path.join(font_dir, chs_font)
    elif kind == en_font:
        path = os.path.join(font_dir, en_font)
    fullpaths = []
    for filename in os.listdir(path):
        fullpath = os.path.join(path, filename)
        if os.path.isfile(fullpath):
            fullpaths.append(fullpath)
    return fullpaths


def gen_random_font(kind, min_size, max_size):
    fullpaths = get_font_fullpaths(kind)
    fullpath = random.choice(fullpaths)
    size = random.randint(min_size, max_size)
    font = ImageFont.truetype(fullpath, size)
    return font


def get_char_sizes(font, chars):
    widths = []
    heights = []
    for idx in range(0, len(chars)):
        char = chars[idx]
        width, height = font.getsize(char)
        widths.append(width)
        heights.append(height)
    return widths, heights
