import sys

import os

sys.path.append(os.path.realpath('..'))

import cv2
import random
import numpy as np
from PIL import Image, ImageDraw
import subprocess

from config.common_config import logger
from config.image_config import min_num_of_chars
from config.image_config import max_num_of_chars
from config.image_config import image_width
from config.image_config import image_height
from config.image_config import image_channels
from config.image_config import black_color
from config.image_config import white_color
from config.image_config import green_color
from config.image_config import line_thickness
from config.image_config import en_font
from config.image_config import font_max_size
from config.image_config import font_min_size

from util.font_util import gen_random_font
from util.font_util import get_char_sizes
from util.string_util import gen_font_chars
from util.file_util import gen_custom_files


def gen_font_image():
    chars = gen_font_chars(min_num_of_chars, max_num_of_chars)
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

    image = Image.new('RGB', (image_width, image_height), black_color)
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
        draw.text(offset, char, font=font, fill=white_color)

    return chars, np.array(image)


def gen_custom_image():
    chars = []
    image = np.zeros((image_height, image_width, image_channels), np.uint8)
    width_offset = 0
    results = gen_custom_files(min_num_of_chars, max_num_of_chars)
    for result in results:
        char = result.get('char')
        fullname = result.get('fullname')
        char_image = cv2.imread(fullname)
        rows, cols, channels = char_image.shape
        width_offset += cols
        logger.debug('--char--' + char)
        if (rows < image_height) and (width_offset + cols < image_width):
            chars.append(char)
            image[0:rows, width_offset:width_offset + cols] = char_image
    return chars, np.array(image)


def crop(src_filename, dst_filename, pt1, pt2):
    src_image = cv2.imread(src_filename)
    logger.debug('--src_image.shape--' + str(src_image.shape))
    x1, y1 = pt1.get('x'), pt1.get('y')
    x2, y2 = pt2.get('x'), pt2.get('y')
    logger.debug('--x1:%s, y1:%s, x2:%s, y2:%s--', str(x1), str(y1), str(x2), str(y2))
    crop_image = src_image[y1:y2, x1:x2]  # [row_start:row_end, col_start:col:end]
    logger.debug('--crop_image.shape--' + str(crop_image.shape))
    cv2.imwrite(dst_filename, crop_image)


def trim(src_filename, dst_filename):
    morphology_cmd = ['convert', src_filename, '-negate', '-define', 'morphology:compose=darken',
                      '-morphology', 'Thinning', 'Rectangle:1x40+0+0<', src_filename]
    subprocess.run(morphology_cmd)
    trim_cmd = ['convert', src_filename, '-fuzz', '10%', '-trim', '+repage', dst_filename]
    subprocess.run(trim_cmd)


def resize(src_filename, dst_filename, width=image_width, height=image_height):
    src_image = cv2.imread(src_filename)
    dst_image = cv2.resize(src_image, (width, height), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(dst_filename, dst_image)


def draw_rectangle(src_filename, dst_filename, pt1, pt2, color=green_color, thickness=line_thickness):
    src_image = cv2.imread(src_filename)
    x1, y1 = pt1.get('x'), pt1.get('y')
    x2, y2 = pt2.get('x'), pt2.get('y')
    dst_image = cv2.rectangle(src_image, (x1, y1), (x2, y2), color, thickness)
    cv2.imwrite(dst_filename, dst_image)
