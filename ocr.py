import sys

import os

sys.path.append(os.path.realpath('..'))

import argparse

from recognition.gen_ocr import train, gen_test_data, evaluate


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
