import sys

import os

sys.path.append(os.path.realpath('..'))

from bson.json_util import dumps
from bson.objectid import ObjectId

from util.mongo_util import get_db
from util.security_util import encrypt_password
from util.security_util import check_password
from config.common_config import logger

db = get_db()
user_collection = db['user']


class User:
    def __init__(self, id, display_name, email, username, password,
                 auth_token, auth_roles, status, create_date, update_date):
        self.id = id
        self.display_name = display_name
        self.email = email
        self.username = username
        self.password = password
        self.auth_token = auth_token
        self.auth_roles = auth_roles
        self.status = status
        self.create_date = create_date
        self.update_date = update_date

    def add_auth_role(self, auth_role):
        self.auth_roles.append(auth_role)


class Role:
    def __init__(self, id, name, introduction):
        self.id = id
        self.name = name
        self.introduction = introduction


def convert_user_from_json(data):
    obj = {}

    id = data.get('id')
    if id and ObjectId.is_valid(id):
        obj['_id'] = ObjectId(id)

    display_name = data.get('display_name')
    if display_name:
        obj['display_name'] = display_name

    email = data.get('email')
    if email:
        obj['email'] = email

    username = data.get('username')
    if username:
        obj['username'] = username

    password = data.get('password')
    if password:
        obj['password'] = password

    auth_token = data.get('auth_token')
    if auth_token:
        obj['auth_token'] = auth_token

    auth_roles = data.get('auth_roles')
    if auth_roles:
        obj['auth_roles'] = auth_roles

    status = data.get('status')
    if status:
        obj['status'] = status

    logger.debug('--obj--' + str(obj))
    return obj


def convert_user_from_mongo(result):
    obj = {}
    obj['id'] = str(result.get('_id'))
    obj['kind'] = result.get('kind')
    obj['display_name'] = result.get('display_name')
    obj['email'] = result.get('email')
    obj['username'] = result.get('username')
    obj['password'] = result.get('password')
    obj['auth_token'] = result.get('auth_token')
    obj['auth_roles'] = result.get('auth_roles')
    obj['status'] = result.get('status')
    return obj


def convert_user_list_from_mongo(results):
    objs = []
    if results:
        for result in results:
            obj = convert_user_from_mongo(result)
            objs.append(obj)
    logger.debug('--objs--' + str(objs))
    return objs


def sign_in_user(data):
    result = None
    if data:
        try:
            username = data.get('username')
            password = data.get('password')
            if username and password:
                existing_user = user_collection.find_one({'username': username})
                hashed_password = existing_user['password']
                if check_password(password, hashed_password):
                    result = existing_user
        except Exception as e:
            logger.debug('--sign_in_user--' + str(e))
    return result


def create_user(data):
    result = None
    if data:
        try:
            obj = convert_user_from_json(data)
            password = obj['password']
            if password:
                obj['password'] = encrypt_password(password)
            obj['status'] = 'create'
            insert_result = user_collection.insert_one(obj)
            id = insert_result.inserted_id
            logger.debug('--id--' + str(id))
            result = get_user(id)
        except Exception as e:
            logger.debug('--create_user--' + str(e))
    return result


def get_user(id):
    result = None
    try:
        result = user_collection.find_one({'_id': id})
        logger.debug('--get_user--' + dumps(result))
    except Exception as e:
        logger.debug('--get_user--' + str(e))
    return result


def list_user(filter, page_request):
    offset = page_request.offset
    sort = page_request.sort
    size = page_request.size
    result = None
    cursor = user_collection.find(filter)
    try:
        if offset:
            cursor.skip(offset)
        if sort:
            cursor.sort(sort)
        if size:
            cursor.limit(size)
        result = list(cursor)
        logger.debug('--list_user--' + dumps(result))
    except Exception as e:
        logger.debug('--list_user--' + str(e))
    return result


def count_user(filter):
    count = None
    try:
        count = user_collection.count(filter)
        logger.debug('--count_user--' + dumps(count))
    except Exception as e:
        logger.debug('--count_user--' + str(e))
    return count


def exist_user(id):
    result = None
    try:
        count = user_collection.count({'_id': id})
        logger.debug('--count--' + str(count))
        if count == 0:
            result = False
        elif count == 1:
            result = True
        logger.debug('--exist_user--' + dumps(result))
    except Exception as e:
        logger.debug('--exist_user--' + str(e))
    return result


def update_user(data):
    result = None
    if data:
        try:
            obj = convert_user_from_json(data)
            id = obj.get('_id')
            logger.debug('--id--' + str(id))
            if exist_user(id):
                del obj['_id']
                user_collection.update_one({'_id': id}, {'$set': obj})
                result = get_user(id)
        except Exception as e:
            logger.debug('--update_user--' + str(e))
    return result


def delete_user(id):
    result = None
    if exist_user(id):
        try:
            user_collection.delete_one({'_id': id})
            if not exist_user(id):
                result = True
        except Exception as e:
            logger.debug('--delete_user--' + str(e))
    return result
