import sys

import os

sys.path.append(os.path.realpath('..'))

import logging

import yaml

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

config = yaml.load(open(os.path.join('config', 'profile.yaml')))

upload_dir = config.get('upload_dir')
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

image_dir = config.get('image_dir')
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

train_dir = config.get('train_dir')
if not os.path.exists(train_dir):
    os.makedirs(train_dir)

evaluate_dir = config.get('evaluate_dir')
if not os.path.exists(evaluate_dir):
    os.makedirs(evaluate_dir)
