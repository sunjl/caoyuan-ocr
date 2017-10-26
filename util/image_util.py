import sys

import os

sys.path.append(os.path.realpath('..'))

import numpy as np
from PIL import Image, ImageFont, ImageDraw

from conf.image import *


def get_font_fullpaths(category):
    path = None
    if category == 'chs':
        path = os.path.join(font_dir, 'chs')
    elif category == 'en':
        path = os.path.join(font_dir, 'en')
    fullpaths = []
    for filename in os.listdir(path):
        fullpath = os.path.join(path, filename)
        if os.path.isfile(fullpath):
            fullpaths.append(fullpath)
    return fullpaths


def gen_image():
    num_of_chars = np.random.randint(min_num_of_chars, max_num_of_chars + 1)
    chars = []
    for idx in range(0, num_of_chars):
        if np.random.uniform() > 0.5:
            digit_idx = np.random.randint(len(digits))
            chars.append(digits[digit_idx])
        else:
            letter_idx = np.random.randint(len(letters))
            chars.append(letters[letter_idx])

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    font_fullpaths = get_font_fullpaths(category='en')
    fullpath_idx = np.random.randint(len(font_fullpaths))
    font_fullpath = font_fullpaths[fullpath_idx]
    font_size = np.random.randint(min_font_size, max_font_size)

    for idx in range(0, len(chars)):
        char = chars[idx]
        font = ImageFont.truetype(font_fullpath, font_size)
        font_width, font_height = font.getsize(char)
        width_offset = idx * font_width
        height_offset_limit = (image_height - font_height) // 2
        if height_offset_limit > 0:
            height_offset = np.random.randint(height_offset_limit)
        else:
            height_offset = 0
        offset = (width_offset, height_offset)
        draw.text(offset, char, font=font, fill=text_color)

    return np.array(image), chars
