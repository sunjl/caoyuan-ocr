import sys

import os

sys.path.append(os.path.realpath('..'))

from flask import Flask, jsonify, make_response, render_template, request
from flask import abort, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


# http://127.0.0.1:5000/json?a=1&b=2
@app.route('/json')
def json():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    query = request.args.get('key', '')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/cookie')
def index():
    username = request.cookies.get('username')
    resp = make_response()
    resp.set_cookie('username', 'the username')


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


# app.secret_key = os.urandom(24)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'test.db'),
    SECRET_KEY='key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('SETTINGS', silent=True)

if __name__ == '__main__':
    app.run()
