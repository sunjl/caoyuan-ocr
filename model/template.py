import sys

import os

sys.path.append(os.path.realpath('..'))

from bson.json_util import dumps
from bson.objectid import ObjectId

from util.mongo_util import get_db
from config.common_config import logger

db = get_db()
template_collection = db['template']


class Template:
    def __init__(self, id, user_id, category, name, regions,
                 storage_id, filename, create_date, update_date):
        self.id = id
        self.user_id = user_id
        self.category = category
        self.name = name
        self.regions = regions
        self.storage_id = storage_id
        self.filename = filename
        self.create_date = create_date
        self.update_date = update_date


def convert_template_from_json(data):
    obj = {}

    id = data.get('id')
    if (id is not None) and ObjectId.is_valid(id):
        obj['_id'] = ObjectId(id)

    user_id = data.get('user_id')
    if user_id and ObjectId.is_valid(user_id):
        obj['user_id'] = ObjectId(user_id)

    obj['category'] = data.get('category')
    obj['name'] = data.get('name')
    obj['regions'] = data.get('regions')

    storage_id = data.get('storage_id')
    if storage_id and ObjectId.is_valid(storage_id):
        obj['storage_id'] = ObjectId(storage_id)

    obj['filename'] = data.get('filename')
    logger.debug('--obj--' + str(obj))
    return obj


def convert_template_from_mongo(result):
    obj = {}
    obj['id'] = str(result.get('_id'))
    obj['user_id'] = str(result.get('user_id'))
    obj['category'] = result.get('category')
    obj['name'] = result.get('name')
    obj['regions'] = result.get('regions')
    obj['storage_id'] = str(result.get('storage_id'))
    obj['filename'] = result.get('filename')
    return obj


def create_template(data):
    result = None
    if data:
        try:
            obj = convert_template_from_json(data)
            insert_result = template_collection.insert_one(obj)
            oid = insert_result.inserted_id
            logger.debug('--oid--' + str(oid))
            result = get_template(oid)
        except Exception as e:
            logger.debug('--create_template--' + str(e))
    return result


def get_template(oid):
    result = None
    try:
        result = template_collection.find_one({'_id': oid})
        logger.debug('--result--' + dumps(result))
    except Exception as e:
        logger.debug('--create_template--' + str(e))
    return result

# templates = template_collection.find({'status': 'waiting'})
# template_collection.update({'_id': template_id}, {'$set': {'status': 'done'}}, False, True)
