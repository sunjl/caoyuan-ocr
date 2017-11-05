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
    def __init__(self, id, user_id, kind, name, regions,
                 storage_id, filename, status, create_date, update_date):
        self.id = id
        self.user_id = user_id
        self.kind = kind
        self.name = name
        self.regions = regions
        self.storage_id = storage_id
        self.filename = filename
        self.status = status
        self.create_date = create_date
        self.update_date = update_date


def convert_template_from_json(data):
    obj = {}

    id = data.get('id')
    if id and ObjectId.is_valid(id):
        obj['_id'] = ObjectId(id)

    user_id = data.get('user_id')
    if user_id and ObjectId.is_valid(user_id):
        obj['user_id'] = ObjectId(user_id)

    kind = data.get('kind')
    if kind:
        obj['kind'] = kind

    name = data.get('name')
    if name:
        obj['name'] = name

    regions = data.get('regions')
    if regions:
        obj['regions'] = regions

    storage_id = data.get('storage_id')
    if storage_id and ObjectId.is_valid(storage_id):
        obj['storage_id'] = ObjectId(storage_id)

    filename = data.get('filename')
    if filename:
        obj['filename'] = filename

    status = data.get('status')
    if status:
        obj['status'] = status

    logger.debug('--obj--' + str(obj))
    return obj


def convert_template_from_mongo(result):
    obj = {}
    obj['id'] = str(result.get('_id'))
    obj['user_id'] = str(result.get('user_id'))
    obj['kind'] = result.get('kind')
    obj['name'] = result.get('name')
    obj['regions'] = result.get('regions')
    obj['storage_id'] = str(result.get('storage_id'))
    obj['filename'] = result.get('filename')
    obj['status'] = result.get('status')
    return obj


def convert_template_list_from_mongo(results):
    objs = []
    if results:
        for result in results:
            obj = convert_template_from_mongo(result)
            objs.append(obj)
    logger.debug('--objs--' + str(objs))
    return objs


def create_template(data):
    result = None
    if data:
        try:
            obj = convert_template_from_json(data)
            obj['status'] = 'create'
            insert_result = template_collection.insert_one(obj)
            id = insert_result.inserted_id
            logger.debug('--id--' + str(id))
            result = get_template(id)
        except Exception as e:
            logger.debug('--create_template--' + str(e))
    return result


def get_template(id):
    result = None
    try:
        result = template_collection.find_one({'_id': id})
        logger.debug('--get_template--' + dumps(result))
    except Exception as e:
        logger.debug('--get_template--' + str(e))
    return result


def list_template(filter, page_request):
    offset = page_request.offset
    sort = page_request.sort
    size = page_request.size
    result = None
    cursor = template_collection.find(filter)
    try:
        if offset:
            cursor.skip(offset)
        if sort:
            cursor.sort(sort)
        if size:
            cursor.limit(size)
        result = list(cursor)
        logger.debug('--list_template--' + dumps(result))
    except Exception as e:
        logger.debug('--list_template--' + str(e))
    return result


def count_template(filter):
    count = None
    try:
        count = template_collection.count(filter)
        logger.debug('--count_template--' + dumps(count))
    except Exception as e:
        logger.debug('--count_template--' + str(e))
    return count


def exist_template(id):
    result = None
    try:
        count = template_collection.count({'_id': id})
        logger.debug('--count--' + str(count))
        if count == 0:
            result = False
        elif count == 1:
            result = True
        logger.debug('--exist_template--' + dumps(result))
    except Exception as e:
        logger.debug('--exist_template--' + str(e))
    return result


def update_template(data):
    result = None
    if data:
        try:
            obj = convert_template_from_json(data)
            id = obj.get('_id')
            logger.debug('--id--' + str(id))
            if exist_template(id):
                del obj['_id']
                template_collection.update_one({'_id': id}, {'$set': obj})
                result = get_template(id)
        except Exception as e:
            logger.debug('--update_template--' + str(e))
    return result


def delete_template(id):
    result = None
    if exist_template(id):
        try:
            template_collection.delete_one({'_id': id})
            if not exist_template(id):
                result = True
        except Exception as e:
            logger.debug('--delete_template--' + str(e))
    return result
