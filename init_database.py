__author__ = 'Gergo'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

BaseClass = declarative_base()


def init(engine):
    db_engine = create_engine(engine, echo=True)
    BaseClass.metadata.create_all(db_engine)
