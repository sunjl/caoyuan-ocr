# _*_ coding: utf-8 _*_

import string

font_dir = '../font'
chs_font = 'chs'
en_font = 'en'
font_max_size = 48
font_min_size = 24

digits = string.digits
letters = string.ascii_letters
dict_chars = digits + letters
dict_classes = int(len(dict_chars))

max_num_of_chars = 5
min_num_of_chars = 1

image_width = 192
image_height = 48
image_channels = 3
background_color = (0, 0, 0)
text_color = (255, 255, 255)
