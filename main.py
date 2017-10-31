import sys

import os

sys.path.append(os.path.realpath('..'))

from flask import Flask

from route.storage_route import storage_app

app = Flask(__name__)

app.register_blueprint(storage_app, url_prefix='/storage')

if __name__ == '__main__':
    app.run()
