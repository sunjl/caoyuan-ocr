import sys

import os

sys.path.append(os.path.realpath('..'))

import json
from flask import request, Response

from config.common_config import logger
from model.storage import store_gridfs
from model.storage import read_gridfs
from model.storage import delete_gridfs

from flask import Blueprint

storage_app = Blueprint('storage_controller', __name__)


@storage_app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return Response(status=400)

    obj = store_gridfs(file)
    if not obj:
        return Response(status=500)

    data = json.dumps(obj)
    logger.debug('--data--' + data)
    resp = Response(response=data, status=201, content_type='application/json')
    return resp


@storage_app.route('/<id>/<name>', methods=['GET'])
def get(id, name):
    if not (id and name):
        return Response(status=400)

    file = read_gridfs(id)
    if not file:
        return Response(status=404)

    filename = file.filename
    data = file.read()
    content_type = file.content_type
    length = file.length
    logger.debug('--filename--' + filename)
    resp = Response(response=data, status=200, content_type=content_type)
    resp.headers['Content-Length'] = length
    resp.headers['Content-Disposition'] = "inline; filename=" + str(filename.encode('utf-8'))
    return resp


@storage_app.route('/delete', methods=['POST'])
def delete():
    data = request.json
    logger.debug('--data--' + str(data))
    file_id = data['id']
    if not file_id:
        return Response(status=400)

    result = delete_gridfs(file_id)
    if result:
        return Response(status=204)
    else:
        return Response(status=202)
