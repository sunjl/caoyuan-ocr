import sys

import os

sys.path.append(os.path.realpath('..'))

from bson.json_util import dumps
from bson.objectid import ObjectId

from util.mongo_util import get_db
from config.common_config import logger

db = get_db()
image_collection = db['image']


class Image:
    def __init__(self, id, user_id, kind, name, template_id, regions,
                 storage_id, filename, status, create_date, update_date):
        self.id = id
        self.user_id = user_id
        self.kind = kind
        self.name = name
        self.template_id = template_id
        self.regions = regions
        self.storage_id = storage_id
        self.filename = filename
        self.status = status
        self.create_date = create_date
        self.update_date = update_date


def convert_image_from_json(data):
    obj = {}

    id = data.get('id')
    if id and ObjectId.is_valid(id):
        obj['_id'] = ObjectId(id)

    user_id = data.get('user_id')
    if user_id and ObjectId.is_valid(user_id):
        obj['user_id'] = ObjectId(user_id)

    template_id = data.get('template_id')
    if template_id and ObjectId.is_valid(template_id):
        obj['template_id'] = ObjectId(template_id)

    obj['regions'] = data.get('regions')

    storage_id = data.get('storage_id')
    if storage_id and ObjectId.is_valid(storage_id):
        obj['storage_id'] = ObjectId(storage_id)

    obj['filename'] = data.get('filename')
    obj['status'] = data.get('status')
    logger.debug('--obj--' + str(obj))
    return obj


def convert_image_from_mongo(result):
    obj = {}
    obj['id'] = str(result.get('_id'))
    obj['user_id'] = str(result.get('user_id'))
    obj['template_id'] = str(result.get('template_id'))
    obj['regions'] = result.get('regions')
    obj['storage_id'] = str(result.get('storage_id'))
    obj['filename'] = result.get('filename')
    obj['status'] = result.get('status')
    return obj


def create_image(data):
    result = None
    if data:
        try:
            obj = convert_image_from_json(data)
            insert_result = image_collection.insert_one(obj)
            id = insert_result.inserted_id
            logger.debug('--id--' + str(id))
            result = get_image(id)
        except Exception as e:
            logger.debug('--create_image--' + str(e))
    return result


def get_image(id):
    result = None
    try:
        result = image_collection.find_one({'_id': id})
        logger.debug('--result--' + dumps(result))
    except Exception as e:
        logger.debug('--create_image--' + str(e))
    return result


def count_image(id):
    count = None
    try:
        count = image_collection.count({'_id': id})
        logger.debug('--count_image--' + dumps(count))
    except Exception as e:
        logger.debug('--count_image--' + str(e))
    return count


def exist_image(id):
    result = None
    try:
        count = image_collection.count({'_id': id})
        logger.debug('--count--' + str(count))
        if count == 0:
            result = False
        elif count == 1:
            result = True
        logger.debug('--exist_image--' + dumps(result))
    except Exception as e:
        logger.debug('--exist_image--' + str(e))
    return result


def delete_image(id):
    result = None
    if not exist_image(id):
        result = False
    else:
        try:
            image_collection.delete_one({'_id': id})
            if not exist_image(id):
                result = True
        except Exception as e:
            logger.debug('--delete_image--' + str(e))
    return result
