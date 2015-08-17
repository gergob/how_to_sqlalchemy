__author__ = 'greg'

from DAL import DAL
import init_database as Init


engine = 'mysql+mysqldb://johndoe:secret@localhost/how_to_sqlalchemy?unix_socket=/opt/lampp/var/mysql/mysql.sock'
my_dal = None

def run_app(should_run_init):
    if should_run_init:
        Init.init(engine)
    else:
        my_dal = DAL(engine)
        my_dal.addUser('John', 'Doe', 'johndoe', 'jd@example.com')


if __name__ == '__main__':
    run_app(True)
    #run_app(False)
