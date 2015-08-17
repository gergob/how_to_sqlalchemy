__author__ = 'greg'

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from BaseClass import BaseClass

class User(BaseClass):
    __tablename__ = 'users'
    user_name = Column(String(150), primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(250))

    bids = relationship('Bid')
