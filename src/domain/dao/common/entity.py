import uuid

from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

from app import db
from sqlalchemy.dialects.postgresql import UUID


BaseEntity = declarative_base()

class IntEntity(object):

    """ Int ID Entity """
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

class UuidEntity(object):

    """ UUID Entity """
    id: UUID = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TimeRecordEntity(object):
    created = db.Column('created', server_default=func.now())
    updated = db.Column('updated', server_default=func.now(), onupdate=func.current_timestamp())


class ValueObject(object):

    """ Value Object """
