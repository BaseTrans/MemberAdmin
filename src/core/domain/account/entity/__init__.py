from app import db
# from sqlalchemy.dialects.postgresql import JSON


class Account(db.Model):

    __tablename__ = 'Account'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    door_num = db.Column(db.Integer())
    cabinet_num = db.Column(db.Integer())
    # result_all = db.Column(JSON)
    # result_no_stop_words = db.Column(JSON)