import sys

import os

sys.path.append(os.path.realpath('..'))

import json
from bson.objectid import ObjectId
from flask import request, Response

from config.common_config import logger
from model.user import sign_in_user
from model.user import create_user
from model.user import get_user
from model.user import list_user
from model.user import count_user
from model.user import update_user
from model.user import delete_user
from model.user import convert_user_from_mongo
from model.user import convert_user_list_from_mongo
from util.page_util import PageRequest
from util.page_util import PageResponse
from util.json_util import PageResponseEncoder

from flask import abort, Blueprint

user_app = Blueprint('user_controller', __name__)


@user_app.route('/sign_in', methods=['POST'])
def sign_in():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    result = sign_in_user(request_data)
    if not result:
        return Response(status=403)

    obj = convert_user_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@user_app.route('/create', methods=['POST'])
def create():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    result = create_user(request_data)
    if not result:
        return Response(status=500)

    obj = convert_user_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@user_app.route('/get', methods=['GET'])
def get():
    id = request.args.get('id')
    if not (id and ObjectId.is_valid(id)):
        abort(400)

    result = get_user(ObjectId(id))
    if not result:
        return Response(status=404)

    obj = convert_user_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@user_app.route('/list', methods=['GET'])
def list():
    filter = {}
    page = None
    size = None
    order = None
    direction = None

    status_arg = request.args.get('status')
    if status_arg:
        filter['status'] = status_arg

    page_arg = request.args.get('page')
    if page_arg:
        page = int(page_arg)

    size_arg = request.args.get('size')
    if size_arg:
        size = int(size_arg)

    order_arg = request.args.get('order')
    if order_arg:
        order = order_arg

    direction_arg = request.args.get('direction')
    if direction_arg:
        if direction_arg is 'asc':
            direction = 1
        elif direction_arg is 'desc':
            direction = -1

    page_request = PageRequest(page, size, order, direction)
    list_result = list_user(filter, page_request)
    count = count_user(filter)

    items = convert_user_list_from_mongo(list_result)
    page_response = PageResponse(page, size, count, items)
    response_data = json.dumps(page_response, cls=PageResponseEncoder)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=200, content_type='application/json')
    return resp


@user_app.route('/update', methods=['POST'])
def update():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    id = request_data.get('id')
    if not id:
        abort(400)

    result = update_user(request_data)
    if not result:
        return Response(status=500)

    obj = convert_user_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=200, content_type='application/json')
    return resp


@user_app.route('/delete', methods=['POST'])
def delete():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    id = request_data.get('id')
    if not (id and ObjectId.is_valid(id)):
        abort(400)

    result = delete_user(ObjectId(id))
    if result:
        return Response(status=204)
    else:
        return Response(status=202)
