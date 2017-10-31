import sys

import os

sys.path.append(os.path.realpath('..'))

import random
import numpy as np
from PIL import Image, ImageDraw

from config.image_config import min_num_of_chars
from config.image_config import max_num_of_chars
from config.image_config import image_width
from config.image_config import image_height
from config.image_config import background_color
from config.image_config import text_color
from config.image_config import en_font
from config.image_config import font_max_size
from config.image_config import font_min_size

from util.font_util import gen_random_font
from util.font_util import get_char_sizes
from util.string_util import gen_chars


def gen_image():
    chars = gen_chars(min_num_of_chars, max_num_of_chars)
    font = gen_random_font(en_font, font_min_size, font_max_size)

    char_widths, char_heights = get_char_sizes(font, chars)
    min_char_width = min(char_widths)
    max_char_width = max(char_widths)

    total_char_width = max_char_width * len(chars)
    width_offset_limit = (image_width - total_char_width) // 2
    if width_offset_limit > 0:
        width_offset = random.randint(1, width_offset_limit)
    else:
        width_offset = 0

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    for char in chars:
        font_width, font_height = font.getsize(char)

        width_offset += random.randint(min_char_width, max_char_width)

        height_offset_limit = (image_height - font_height) // 2
        if height_offset_limit > 0:
            height_offset = random.randint(1, height_offset_limit)
        else:
            height_offset = 0

        offset = (width_offset, height_offset)
        draw.text(offset, char, font=font, fill=text_color)

    return chars, np.array(image)
