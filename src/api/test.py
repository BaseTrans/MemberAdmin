import uuid

from flask import Blueprint

import app
from domain.dao.account import Account
from infra.orm.sqlalchemy_adapter.repository import SqlAlchemyRepository

test = Blueprint('test', __name__)

@test.route('/')
def hello_world():
    return 'Hello World!'

@test.route('/account')
def add_user():
    account = Account(
        # id=uuid.uuid4(),
        name='bbb',
        is_active= True,
        door_id=236,
        cabinet_num = '1222'
    )

    repo = SqlAlchemyRepository("postgresql://postgres:23322335@localhost:5432/TransBase")
    repo.create(account)
    return 'add_user'
