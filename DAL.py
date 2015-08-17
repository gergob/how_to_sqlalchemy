__author__ = 'Gergo'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Bid import Bid
from Project import Project
from User import User


class DAL:
    def __init__(self, engine):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def add_user(self, first_name, last_name, user_name, email):
        """
        :type first_name: string
        :type last_name: string
        :type user_name: string
        :type email: string
        """
        new_user = User(user_name=user_name,
                        first_name=first_name,
                        last_name=last_name,
                        email=email)
        self.session.add(new_user)
        self.session.commit()

    def clear_users(self):
        all_users = self.session.query(User)
        for user in all_users:
            self.session.delete(user)
        self.session.commit()

    def get_users(self):
        all_users = self.session.query(User).order_by(User.user_name)
        return all_users

    def search_users(self, user_name):
        all_users = self.session.query(User).filter(User.user_name.like('%' + user_name + '%'))
        return all_users
