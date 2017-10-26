import argparse
import shutil
import string

import cv2
import numpy as np
import os
import pandas as pd
import tensorflow as tf
from PIL import Image, ImageFont, ImageDraw
from keras.callbacks import EarlyStopping
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Activation, Flatten
from keras.layers import Input
from keras.models import Model
from keras.optimizers import Adadelta
from keras.utils import plot_model

digits = string.digits
letters = string.ascii_letters
dict_chars = digits + letters
dict_classes = int(len(dict_chars))

font_dir = '../font'
max_num_of_chars = 5
min_num_of_chars = 1
image_width = 192
image_height = 48
background_color = (0, 0, 0)
text_color = "#ffffff"
max_font_size = 48
min_font_size = 24

num_epoch = 500
input_shape = (image_height, image_width, 3)
batch_size = 32
patience = 10
model_dir = '../model'
model_h5_name = 'output.h5'
model_plot_name = 'output.png'
test_data_dir = '../data/test'
test_data_size = 10


def get_font_fullpaths(category):
    path = None
    if category == 'chs':
        path = os.path.join(font_dir, 'chs')
    elif category == 'en':
        path = os.path.join(font_dir, 'en')
    fullpaths = []
    for filename in os.listdir(path):
        fullpath = os.path.join(path, filename)
        if os.path.isfile(fullpath):
            fullpaths.append(fullpath)
    return fullpaths


def gen_image():
    num_of_chars = np.random.randint(min_num_of_chars, max_num_of_chars + 1)
    chars = []
    for idx in range(0, num_of_chars):
        if np.random.uniform() > 0.5:
            digit_idx = np.random.randint(len(digits))
            chars.append(digits[digit_idx])
        else:
            letter_idx = np.random.randint(len(letters))
            chars.append(letters[letter_idx])

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    font_fullpaths = get_font_fullpaths(category='en')
    fullpath_idx = np.random.randint(len(font_fullpaths))
    font_fullpath = font_fullpaths[fullpath_idx]
    font_size = np.random.randint(min_font_size, max_font_size)

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

    return np.array(image), chars


def batch_generator(size):
    while True:
        image_list = []
        head1_list = []
        head2_list = []
        for i in range(size):
            image, chars = gen_image()
            chars_length = len(chars)

            head1 = np.zeros((max_num_of_chars * dict_classes), np.int32)
            head2 = np.zeros((max_num_of_chars - min_num_of_chars + 1), np.int32)

            for idx in range(0, chars_length):
                char = chars[idx]
                head1[idx * dict_classes + dict_chars.index(char)] = 1
                head2[chars_length - min_num_of_chars] = 1

            image_list.append(image)
            head1_list.append(head1)
            head2_list.append(head2)

        image_arr = np.array(image_list, dtype=np.float32)
        head1_arr = np.array(head1_list, dtype=np.int32)
        head2_arr = np.array(head2_list, dtype=np.int32)

        yield (image_arr, {'head1': head1_arr, 'head2': head2_arr})


def custom_loss(y_true, y_pred):
    labels = tf.reshape(y_true[:, :max_num_of_chars * dict_classes],
                        [batch_size, max_num_of_chars, dict_classes])

    logits = tf.reshape(y_pred[:, :max_num_of_chars * dict_classes],
                        [batch_size, max_num_of_chars, dict_classes])

    mask = tf.reduce_sum(labels, -1)
    loss = tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits)
    loss = loss * mask
    loss = tf.reduce_sum(loss)
    return loss


def custom_cross_entropy(y_true, y_pred):
    loss = tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_pred)
    return loss


def get_model():
    input_data = Input(shape=input_shape)

    conv1 = Conv2D(32, (3, 3), padding='same')(input_data)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    act1 = Activation('relu')(pool1)

    conv2 = Conv2D(32, (3, 3), padding='same')(act1)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    act2 = Activation('relu')(pool2)

    conv3 = Conv2D(64, (3, 3), padding='same')(act2)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    act3 = Activation('relu')(pool3)

    conv4 = Conv2D(64, (3, 3), padding='same')(act3)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)
    act4 = Activation('relu')(pool4)

    flatten = Flatten()(act4)

    head1 = Dense(max_num_of_chars * dict_classes, name='head1')(flatten)
    head2 = Dense(max_num_of_chars - min_num_of_chars + 1, name='head2')(flatten)

    model = Model(inputs=input_data, outputs=[head1, head2])
    model.compile(optimizer=Adadelta(), loss={'head1': custom_loss, 'head2': custom_cross_entropy})

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    print(model.summary())
    plot_model(model, to_file=os.path.join(model_dir, model_plot_name), show_shapes=True)

    return model


def train(epochs=num_epoch):
    model = get_model()

    callbacks = [
        EarlyStopping(monitor='val_loss', patience=patience, verbose=0)
    ]

    history = model.fit_generator(
        generator=batch_generator(batch_size),
        steps_per_epoch=batch_size,
        epochs=epochs,
        verbose=2,
        callbacks=callbacks,
        validation_data=batch_generator(batch_size),
        validation_steps=batch_size)

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model.save_weights(os.path.join(model_dir, model_h5_name))
    pd.DataFrame(history.history).to_csv(os.path.join(model_dir, 'train_history.csv'), index=False)


def gen_test_data(size=test_data_size):
    if os.path.exists(test_data_dir):
        shutil.rmtree(test_data_dir)
    os.makedirs(test_data_dir)

    for i in range(0, size):
        img, chars = gen_image()
        name = ''.join(char for char in chars)
        cv2.imwrite(os.path.join(test_data_dir, name + '.png'), img)


def decode_prediction(y_pred):
    char_str = []

    y_pred_head1 = y_pred[0]
    y_pred_head2 = y_pred[1]

    pred_num = np.argmax(y_pred_head2) + min_num_of_chars
    print("predicted number of chars:", pred_num)

    for i in range(0, pred_num):
        idx = np.argmax(y_pred_head1[:, i * dict_classes:(i + 1) * dict_classes])
        char_str.append(dict_chars[idx])

    print('prediction:', char_str)


def evaluate():
    model = get_model()
    model.load_weights(os.path.join(model_dir, model_h5_name))

    for filename in sorted(os.listdir(test_data_dir)):
        image_path = os.path.join(test_data_dir, filename)
        print('image path:', image_path)

        img = cv2.imread(image_path)

        y_pred = model.predict(img[None, ...])

        decode_prediction(y_pred)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('task')
    parser.add_argument('-i', '--input', required=False)
    args = parser.parse_args()
    task = args.task
    if task == 'train':
        train()
    elif task == 'gen_test_data':
        gen_test_data()
    elif task == 'evaluate':
        evaluate()


if __name__ == "__main__":
    main()
