__author__ = 'greg'

from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from BaseClass import BaseClass

class Bid(BaseClass):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    proposal = Column(String(800))
    price = Column(Numeric)
    user_id = Column(String(150), ForeignKey('users.user_name'))
    project_id = Column(Integer, ForeignKey('projects.id'))


