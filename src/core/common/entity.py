import uuid

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


class ValueObject(object):

    """ Value Object """
