import sys

import os

sys.path.append(os.path.realpath('.'))

from flask import Flask
from flask_cors import CORS

from route.user_route import user_app
from route.storage_route import storage_app
from route.template_route import template_app
from route.image_route import image_app

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(user_app, url_prefix='/user')
app.register_blueprint(storage_app, url_prefix='/storage')
app.register_blueprint(template_app, url_prefix='/template')
app.register_blueprint(image_app, url_prefix='/image')

if __name__ == '__main__':
    app.run()
