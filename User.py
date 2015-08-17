__author__ = 'Gergo'

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseClass = declarative_base()

class User(BaseClass):
    __tablename__ = 'users'
    user_name = Column(String(150), primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(250))

    bids = relationship('Bid', backref='user')
