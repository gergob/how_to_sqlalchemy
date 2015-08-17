__author__ = 'greg'

from sqlalchemy import Column, String, Integer, ForeignKey, Numeric

from sqlalchemy.orm import relationship, backref


from BaseClass import BaseClass



class Project(BaseClass):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(150))
    description = Column(String(800))
    budget = Column(Numeric)

    bids = relationship('Bid')
