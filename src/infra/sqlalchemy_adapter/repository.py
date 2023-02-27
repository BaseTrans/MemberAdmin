from sqlalchemy.orm import sessionmaker
from src.infra.db_interface.repository import IRepository

from app import db

class SqlAlchemyRepository(IRepository):

    def __init__(self):
        self.engine = db.engine
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
