import sys

import os

sys.path.append(os.path.realpath('..'))

import logging

import yaml

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

config = yaml.load(open(os.path.join('config', 'profile.yaml')))

upload_dir = config['upload_dir']
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

image_dir = config['image_dir']
if not os.path.exists(image_dir):
    os.makedirs(image_dir)
