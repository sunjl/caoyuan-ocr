import sys

import os

sys.path.append(os.path.realpath('..'))

import mimetypes
import gridfs

from util.mongo_util import get_db
from config.common_config import logger
from config.common_config import upload_dir

db = get_db()
gfs = gridfs.GridFS(db)


def store_fs(file):
    fullname = None
    if file:
        try:
            filename = file.filename
            fullname = os.path.join(upload_dir, filename)
            file.save(fullname)
        except Exception as e:
            logger.debug('--store_fs--' + str(e))
    return fullname


def store_gridfs(file):
    obj = None
    if file:
        try:
            filename = file.filename
            extension = filename.split('.')[-1]
            content_type = mimetypes.types_map['.' + extension]
            id = gfs.put(file, filename=filename, content_type=content_type)
            logger.debug('--id--' + str(id))
            read_file = read_gridfs(id)
            obj = {
                'id': str(id),
                'filename': read_file.filename,
                'content_type': read_file.content_type,
                'length': read_file.length
            }
        except Exception as e:
            logger.debug('--store_gridfs--' + str(e))
    return obj


def read_gridfs(id):
    file = None
    try:
        file = gfs.get(id)
    except Exception as e:
        logger.debug('--read_gridfs--' + str(e))
    return file


def delete_gridfs(id):
    result = None
    try:
        gfs.delete(id)
        result = True
    except Exception as e:
        logger.debug('--delete_gridfs--' + str(e))
        result = False
    return result
