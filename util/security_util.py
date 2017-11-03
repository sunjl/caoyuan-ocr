import sys

import os

sys.path.append(os.path.realpath('..'))

import bcrypt


def encrypt_password(password):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed_password


def check_password(password, hashed_password):
    result = bcrypt.checkpw(password, hashed_password)
    return result
