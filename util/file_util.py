import sys

import os

sys.path.append(os.path.realpath('..'))

import random

from config.common_config import logger
from config.common_config import image_dir
from config.image_config import train_kind
from config.image_config import regions


def gen_custom_files(min_size, max_size):
    train_image_path = os.path.join(image_dir, train_kind)
    dirs = os.listdir(train_image_path)
    dir = random.choice(dirs)
    regions_dir = os.path.join(train_image_path, dir, regions)
    filenames = os.listdir(regions_dir)

    results = []
    size = random.randint(min_size, max_size)
    for idx in range(0, size):
        filename = random.choice(filenames)
        root, ext = os.path.splitext(filename)
        fullname = os.path.join(regions_dir, filename)
        result = {'char': root, 'fullname': fullname}
        results.append(result)
    logger.debug('--results--' + str(results))
    return results
