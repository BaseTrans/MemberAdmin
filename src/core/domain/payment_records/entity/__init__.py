from app import db

class PaymentRecords(db.Model):

    __tablename__ = 'PaymentRecords'

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String()) # ForeignKey

    account_id = db.Column(db.Integer, db.ForeignKey('Account.id'), nullable=False)
