from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from api.test import test


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:23322335@localhost:5432/TransBase"

db = SQLAlchemy(app)

from domain.dao import account
from domain.dao import bank_record
from domain.dao import payment_record

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/test')
def fun():
    sql_cmd = """select * from table1"""

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    print(query_data.first()[1])
    return 'ok'


app.register_blueprint(test)

if __name__ == '__main__':
    app.run()
