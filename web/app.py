import sys

import os

sys.path.append(os.path.realpath('..'))

import json
from flask import Flask, request, Response

from web.config import logger
from web.storage import store_gridfs
from web.storage import read_gridfs
from web.storage import delete_gridfs

app = Flask(__name__)


@app.route('/storage/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return Response(status=400)

    obj = store_gridfs(file)
    if not obj:
        return Response(status=500)

    data = json.dumps(obj)
    logger.debug('----data----' + data)
    resp = Response(response=data, status=201, content_type='application/json')
    return resp


@app.route('/storage/<id>/<name>', methods=['GET'])
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
    logger.debug('----filename----' + filename)
    resp = Response(response=data, status=200, content_type=content_type)
    resp.headers['Content-Length'] = length
    resp.headers['Content-Disposition'] = "inline; filename=" + str(filename.encode('utf-8'))
    return resp


@app.route('/storage/delete', methods=['POST'])
def delete():
    data = request.json
    logger.debug('----data----' + str(data))
    file_id = data['id']
    if not file_id:
        return Response(status=400)

    result = delete_gridfs(file_id)
    if result:
        return Response(status=204)
    else:
        return Response(status=202)


if __name__ == '__main__':
    app.run()
