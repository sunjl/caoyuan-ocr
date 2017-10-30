# _*_ coding: utf-8 _*_

import sys

import os

sys.path.append(os.path.realpath('..'))

import random

from conf.image_conf import digits
from conf.image_conf import letters


def gen_chars(min_size, max_size):
    chars = []
    size = random.randint(min_size, max_size)
    for idx in range(0, size):
        if random.uniform(0, 1) > 0.5:
            chars.append(random.choice(digits))
        else:
            chars.append(random.choice(letters))
    return chars
