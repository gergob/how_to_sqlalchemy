__author__ = 'Gergo'

from DAL import DAL
import init_database as Init

engine = 'mysql://johndoe:secret@localhost/how_to_sqlalchemy'
my_dal = None

def run_app(should_run_init):
    if should_run_init:
        Init.init(engine)
    else:
        my_dal = DAL(engine)

if __name__ == '__main__':
    run_app(True)
