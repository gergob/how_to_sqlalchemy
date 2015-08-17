__author__ = 'Gergo'


from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base

BaseClass = declarative_base()

class Bid(BaseClass):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    proposal = Column(String)
    price = Column(Numeric)
    user_id = Column(String(150), ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))

