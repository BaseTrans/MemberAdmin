from datetime import datetime

from app import db
from .common.entity import UuidEntity, BaseEntity
from .payment_record import PaymentRecord


class Account(BaseEntity, UuidEntity, db.Model):

    __tablename__ = 'Accounts'

    name = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    door_id = db.Column(db.Integer())
    cabinet_num = db.Column(db.String())

    db_account_payment_records = db.relationship("PaymentRecord", backref="Accounts")
    db_account_payment_info = db.relationship("PaymentInfo", backref="Accounts")
