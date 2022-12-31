from app import db
from datetime import datetime


class BankRecords(db.Model):

    __tablename__ = 'BankRecords'

    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime, nullable=False)
    account_date = db.Column(db.DateTime, nullable=False)
    summary = db.Column(db.String)
    transaction_amount = db.Column(db.Numeric, nullable=False)
    balance = db.Column(db.Numeric, nullable=False)
    remark = db.Column(db.String)
