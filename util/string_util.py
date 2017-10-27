import sys

import os

sys.path.append(os.path.realpath('..'))

import numpy as np

from conf.image_conf import digits
from conf.image_conf import letters


def gen_chars(min_size, max_size):
    chars = []
    size = np.random.randint(min_size, max_size + 1)
    for idx in range(0, size):
        if np.random.uniform() > 0.5:
            digit_idx = np.random.randint(len(digits))
            chars.append(digits[digit_idx])
        else:
            letter_idx = np.random.randint(len(letters))
            chars.append(letters[letter_idx])
    return chars
