from sqlalchemy import create_engine

import app
from sqlalchemy.orm import sessionmaker

from src.infra.db_interface.repository import IRepository

# Base = declarative_base()
#
#
# class Entity(Base):
#     """Base class for SQLAlchemy entities"""
#     __abstract__ = True
#
#     id = Column(Integer, primary_key=True)
#
#
# class MyEntity(Entity):
#     """An example SQLAlchemy entity"""
#     __tablename__ = "my_entity"
#
#     name = Column(String)


class SqlAlchemyRepository(IRepository):
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_by_pkey(self, pkey, entity):
        return self.session.query(entity).get(pkey)

    def update(self, entity):
        self.session.commit()

    def remove(self, entity):
        self.session.delete(entity)
        self.session.commit()
