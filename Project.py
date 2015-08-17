__author__ = 'Gergo'

from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseClass = declarative_base()

class Project(BaseClass):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(150))
    description = Column(String)
    budget = Column(Numeric)

    bids = relationship('Bid', backref='project')
