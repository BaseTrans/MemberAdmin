from sqlalchemy.dialects.postgresql import UUID

from app import db
from .common.entity import IntEntity, BaseEntity



class PaymentRecord(BaseEntity, IntEntity, db.Model):

    __tablename__ = 'PaymentRecords'

    transaction_id = db.Column(db.Integer, db.ForeignKey('BankRecords.id'))
    account_id: UUID = db.Column(UUID(as_uuid=True), db.ForeignKey('Accounts.id'))
