__author__ = 'Gergo'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Bid import Bid
from Project import Project
from User import User


class DAL:
    def __init__(self, engine):
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind = db_engine)
        self.session = db_session()

    def addUser(self, first_name, last_name, user_name, email):
        """

        :type email: string
        """
        new_user = User(user_name = user_name,
                        first_name = first_name,
                        last_name = last_name,
                        email = email)
