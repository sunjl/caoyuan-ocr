import sys

import os

sys.path.append(os.path.realpath('..'))

import bcrypt


def encrypt_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def check_password(password, hashed_password):
    result = bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8'))
    return result
