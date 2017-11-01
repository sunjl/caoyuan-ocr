import sys

import os

sys.path.append(os.path.realpath('..'))

import json
from bson.objectid import ObjectId
from flask import request, Response

from config.common_config import logger
from model.image import create_image
from model.image import get_image
from model.image import update_image
from model.image import delete_image
from model.image import convert_image_from_mongo

from flask import Blueprint

image_app = Blueprint('image_controller', __name__)


@image_app.route('/create', methods=['POST'])
def create():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    storage_id = request_data.get('storage_id')
    if not storage_id:
        return Response(status=400)

    result = create_image(request_data)
    if not result:
        return Response(status=500)

    obj = convert_image_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@image_app.route('/get', methods=['GET'])
def get():
    id = request.args.get('id')
    if not (id and ObjectId.is_valid(id)):
        return Response(status=400)

    result = get_image(ObjectId(id))
    if not result:
        return Response(status=404)

    obj = convert_image_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=201, content_type='application/json')
    return resp


@image_app.route('/update', methods=['POST'])
def update():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    id = request_data.get('id')
    if not id:
        return Response(status=400)

    result = update_image(request_data)
    if not result:
        return Response(status=500)

    obj = convert_image_from_mongo(result)
    response_data = json.dumps(obj)
    logger.debug('--response_data--' + response_data)
    resp = Response(response=response_data, status=200, content_type='application/json')
    return resp


@image_app.route('/delete', methods=['POST'])
def delete():
    request_data = request.json
    logger.debug('--request_data--' + str(request_data))
    id = request_data.get('id')
    if not (id and ObjectId.is_valid(id)):
        return Response(status=400)

    result = delete_image(ObjectId(id))
    if result:
        return Response(status=204)
    else:
        return Response(status=202)
