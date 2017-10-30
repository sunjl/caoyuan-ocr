# _*_ coding: utf-8 _*_

import sys

import os

sys.path.append(os.path.realpath('..'))

from web.config import logger
from web.storage import store_gridfs
from web.storage import read_gridfs
from web.storage import delete_gridfs
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


@app.route('/storage/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        oid = store_gridfs(file)
        if oid:
            id = str(oid)
            return jsonify(id=id)


@app.route('/storage/<id>/<name>', methods=['GET'])
def get(id, name):
    file = read_gridfs(id)
    bytes = file.read()
    filename = file.filename
    content_type = file.content_type
    length = file.length
    logger.debug('----filename----' + filename)
    resp = make_response(bytes)
    resp.headers['Content-Type'] = "application/octet-stream"
    resp.headers['Content-Disposition'] = "inline; filename=" + filename
    return resp


@app.route('/storage/delete', methods=['POST'])
def delete():
    resp = None
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.json
        logger.debug('----data----' + str(data))
        file_id = data['id']
        result = delete_gridfs(file_id)
        resp = make_response()
    return resp


if __name__ == '__main__':
    app.run()
