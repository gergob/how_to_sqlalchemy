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

    def __init__(self, user_name, first_name, last_name, email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
