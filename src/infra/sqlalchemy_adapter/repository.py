from abc import ABC, abstractmethod
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.infra.db_interface.repository import IRepository


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
