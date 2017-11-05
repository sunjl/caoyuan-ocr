import sys

import os

sys.path.append(os.path.realpath('..'))

from json import JSONEncoder

from util.page_util import PageRequest
from util.page_util import PageResponse


class PageRequestEncoder(JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, PageRequest):
            return super(PageRequestEncoder, self).default(obj)
        return obj.__dict__


class PageResponseEncoder(JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, PageResponse):
            return super(PageResponseEncoder, self).default(obj)
        return obj.__dict__
