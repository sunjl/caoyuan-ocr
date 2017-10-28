import sys

import os

sys.path.append(os.path.realpath('..'))

import random
import numpy as np

from conf.image_conf import digits
from conf.image_conf import letters


def gen_chars(min_size, max_size):
    chars = []
    size = np.random.randint(min_size, max_size + 1)
    for idx in range(0, size):
        if np.random.uniform() > 0.5:
            chars.append(random.choice(digits))
        else:
            chars.append(random.choice(letters))
    return chars
