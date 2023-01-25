from app import db

from core.common.entity import IntEntity, BaseEntity


class BankRecords(BaseEntity, IntEntity, db.Model):

    __tablename__ = 'BankRecords'

    transaction_date = db.Column(db.DateTime, nullable=False)
    account_date = db.Column(db.DateTime, nullable=False)
    summary = db.Column(db.String)
    transaction_amount = db.Column(db.Numeric, nullable=False)
    balance = db.Column(db.Numeric, nullable=False)
    remark = db.Column(db.String)
