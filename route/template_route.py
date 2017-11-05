import sys

import os

sys.path.append(os.path.realpath('..'))

import json
from bson.objectid import ObjectId
from flask import request, Response

from config.common_config import logger
from model.template import create_template
from model.template import get_template
from model.template import list_template
from model.template import count_template
from model.template import update_template
from model.template import delete_template
from model.template import convert_template_from_mongo
from model.template import convert_template_list_from_mongo
from util.page_util import PageRequest
from util.page_util import PageResponse
from util.json_util import PageResponseEncoder

from flask import abort, Blueprint

template_app = Blueprint('template_controller', __name__)


@template_app.route('/create', methods=['POST'])
def create():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    storage_id = request_data.get('storage_id')
    if not storage_id:
        abort(400)

    result = create_template(request_data)
    if not result:
        return Response(status=500)

    obj = convert_template_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@template_app.route('/get', methods=['GET'])
def get():
    id = request.args.get('id')
    if not (id and ObjectId.is_valid(id)):
        abort(400)

    result = get_template(ObjectId(id))
    if not result:
        return Response(status=404)

    obj = convert_template_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@template_app.route('/list', methods=['GET'])
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
    list_result = list_template(filter, page_request)
    count = count_template(filter)

    items = convert_template_list_from_mongo(list_result)
    page_response = PageResponse(page, size, count, items)
    response_data = json.dumps(page_response, cls=PageResponseEncoder)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=200, content_type='application/json')
    return resp


@template_app.route('/update', methods=['POST'])
def update():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    id = request_data.get('id')
    if not id:
        abort(400)

    result = update_template(request_data)
    if not result:
        return Response(status=500)

    obj = convert_template_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=200, content_type='application/json')
    return resp


@template_app.route('/delete', methods=['POST'])
def delete():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    id = request_data.get('id')
    if not (id and ObjectId.is_valid(id)):
        abort(400)

    result = delete_template(ObjectId(id))
    if result:
        return Response(status=204)
    else:
        return Response(status=202)
