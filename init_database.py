__author__ = 'greg'

from sqlalchemy import create_engine
from BaseClass import BaseClass


def init(engine):
    db_engine = create_engine(engine, echo=True)
    BaseClass.metadata.create_all(db_engine)
