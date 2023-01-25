import uuid

from sqlalchemy.dialects.postgresql import UUID

from app import db
from core.common.entity import IntEntity, BaseEntity



class PaymentRecords(BaseEntity, IntEntity, db.Model):

    __tablename__ = 'PaymentRecords'

    transaction_id = db.Column(db.String()) # ForeignKey
    account_id: UUID = db.Column(UUID(as_uuid=True), db.ForeignKey('Account.id'))
