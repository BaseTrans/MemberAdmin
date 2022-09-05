from flask import Blueprint

test = Blueprint('test', __name__)


@test.route('/')
def hello_world():
    return 'Hello World!'

