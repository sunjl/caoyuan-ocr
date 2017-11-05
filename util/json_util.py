import sys

import os

sys.path.append(os.path.realpath('..'))

from json import JSONEncoder

from util.page_util import PageResponse


class PageResponseEncoder(JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, PageResponse):
            return super(PageResponseEncoder, self).default(obj)
        return obj.__dict__
