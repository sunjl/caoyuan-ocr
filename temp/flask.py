# -*- coding: utf-8 -*-

def read_file(filename, charset='utf-8'):
    with open(filename, 'r') as f:
        return f.read().decode(charset)

def write_file(filename, contents, charset='utf-8'):
    with open(filename, 'w') as f:
        f.write(contents.encode(charset))

filename = os.path.join(app.instance_path, 'application.cfg')
with open(filename) as f:
    config = f.read()

# or via open_instance_resource:
with app.open_instance_resource('application.cfg') as f:
    config = f.read()

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def user_search(request):
    name = request.GET.get('name').strip()
    user_list = list()
    if name:
        user_list = User.get_by_name(name)

class User(object):
    @classmethod
    def get_by_name(cls, name):
        return DBSession.query(cls).filter(cls.name==name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/login', methods=['POST', 'GET'])
def login():
    query = request.args.get('key', '')


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

from flask import Response
r = Response(response="TEST OK", status=200, mimetype="application/xml")
r.headers["Content-Type"] = "text/xml; charset=utf-8"
return r


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = TextField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)
    name = db.Column(db.String(80))

    def get_security_payload(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


from flask.wtf import Form, TextField, PasswordField, validators
from myapplication.models import User


class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

from flask import flash, redirect, url_for, session, render_template

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(u'Successfully logged in as %s' % form.user.username)
        session['user_id'] = form.user.id
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

from flask_validator import ValidateInteger, ValidateString, ValidateEmail

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    code = db.Column(db.Integer())
    email = db.Column(db.String(125))

    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

    @classmethod
    def __declare_last__(cls):
        ValidateString(User.name)
        ValidateInteger(User.code)
        ValidateEmail(User.email)

user = User('Arthur Dent', 42, 'arthur@babelfish.org')

user.name = 666
print user.name
user.name = 'Zaphod Beeblebrox'
print user.name

from flask_validator import Validator

class ValidateAorB(Validator)
    def __init__(self, field, useless, allow_null=True, throw_exception=False, message=None):
        self.useless = useless

        Validator.__init__(self, field, allow_null, throw_exception, message):

    def check_value(self, value):
        retunr if value in ['A', 'B']

class ValidateA(Validator)
    def check_value(self, value):
        retunr if value == 'A'

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    code = db.Column(db.Integer())
    email = db.Column(db.String(125))

    def __init__(self, string, integer):
        self.string = string
        self.integer = integer

validate =  ValidateString(User.name)
validate.stop()
validate.start()

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):

posts.find_one({"author": "Mike"})

posts.find_one({"_id": post_id})

document = client.db.collection.find_one({'_id': ObjectId(post_id)})

posts.find({"author": "Mike"}).count()
db.test.count({'x': 1})
result = db.test.delete_one({'x': 1})
result.deleted_count
db.test.count({'x': 1})
self.__files.delete_one({"_id": file_id})
self.__chunks.delete_many({"files_id": file_id})

result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
sorted(list(db.profiles.index_information()))

db.objects.insert_one({"last_modified": datetime.datetime.utcnow()})

import pytz
pacific = pytz.timezone('US/Pacific')
aware_datetime = pacific.localize(datetime.datetime(2002, 10, 27, 6, 0, 0))
result = db.times.insert_one({"date": aware_datetime})
db.times.find_one()['date']

























