import string

font_dir = 'font'
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
black_color = (0, 0, 0)
white_color = (255, 255, 255)
green_color = (0, 255, 0)
line_thickness = 1

train_kind = 'train'
evaluate_kind = 'evaluate'
regions = 'regions'
