from datetime import datetime

from app import db
from core.common.entity import UuidEntity, BaseEntity



class Account(BaseEntity, UuidEntity, db.Model):

    __tablename__ = 'Account'

    name = db.Column(db.String())
    door_id = db.Column(db.Integer())
    cabinet_num = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    charge_amount_per_month = db.Column(db.Float())
    last_pay_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_pay_amount = db.Column(db.Float())
    next_pay_date = db.Column(db.DateTime, default=datetime.utcnow)

    db_product_payment_records = db.relationship("PaymentRecords", backref="Account")
    # def __init__(self):
    #     super().__init__()