import sys

import os

sys.path.append(os.path.realpath('..'))

import numpy as np
from PIL import Image, ImageFont, ImageDraw

from conf.image_conf import min_num_of_chars
from conf.image_conf import max_num_of_chars
from conf.image_conf import image_width
from conf.image_conf import image_height
from conf.image_conf import background_color
from conf.image_conf import text_color
from conf.image_conf import chs_font
from conf.image_conf import font_max_size
from conf.image_conf import font_min_size

from util.font_util import gen_random_font
from util.string_util import gen_chars


def gen_image():
    chars = gen_chars(min_num_of_chars, max_num_of_chars)
    font_fullpath, font_size = gen_random_font(chs_font, font_min_size, font_max_size)

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

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

    return chars, np.array(image)
