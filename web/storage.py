# _*_ coding: utf-8 _*_

import sys

import os

sys.path.append(os.path.realpath('..'))

from web.config import logger
from web.config import upload_dir
import gridfs
from bson.objectid import ObjectId

from  util.mongo_util import get_conn

conn = get_conn()
gfs = gridfs.GridFS(conn)


def store_fs(file):
    fullname = None
    if file:
        try:
            filename = file.filename
            fullname = os.path.join(upload_dir, filename)
            file.save(fullname)
            logger.debug('----fullname----' + fullname)
        except Exception as e:
            logger.debug('----store_fs----' + str(e))
    return fullname


def store_gridfs(file):
    oid = None
    if file:
        try:
            filename = file.filename
            oid = gfs.put(file, filename=filename)
            logger.debug('----oid----' + str(oid))
        except Exception as e:
            logger.debug('----store_gridfs----' + str(e))
    return oid


def read_gridfs(id):
    file = None
    if id and ObjectId.is_valid(id):
        try:
            file = gfs.get(ObjectId(id))
        except Exception as e:
            logger.debug('----read_gridfs----' + str(e))
    return file


def delete_gridfs(id):
    result = None
    if id and ObjectId.is_valid(id):
        try:
            gfs.delete(ObjectId(id))
            result = True
        except Exception as e:
            logger.debug('----delete_gridfs----' + str(e))
            result = False
    return result
