import sys

import os

sys.path.append(os.path.realpath('..'))

from math import ceil


class PageRequest(object):
    def __init__(self, page, size, field, direction):
        if not page or page < 0:
            self.page = 0
        else:
            self.page = page

        if not size or size < 0:
            self.size = 10
        elif size > 100:
            self.size = 100
        else:
            self.size = size

        self.offset = page * size

        if direction and direction in [1, -1]:
            self.sort = (field, direction)
        else:
            self.sort = field


class PageResponse(object):
    def __init__(self, page, size, count, items):
        self.page = page
        self.size = size
        self.count = count
        self.items = items

    @property
    def pages(self):
        return int(ceil(self.count / float(self.size)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages
