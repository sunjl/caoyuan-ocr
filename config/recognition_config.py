import sys

import os

sys.path.append(os.path.realpath('..'))

from config.image_config import image_width
from config.image_config import image_height

num_epoch = 100
grayscale_input_shape = (image_height, image_width, 1)
color_input_shape = (image_height, image_width, 3)
batch_size = 128
patience = 10
output_dir = 'output'
model_h5_name = 'model.h5'
model_plot_name = 'model.png'
test_data_dir = '/data2/application/caoyuan_ocr/test'
test_data_size = 10
