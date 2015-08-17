__author__ = 'greg'

from DAL import DAL
import init_database as Init


engine = 'mysql+mysqldb://johndoe:secret@localhost/how_to_sqlalchemy?unix_socket=/opt/lampp/var/mysql/mysql.sock'
my_dal = None


def add_users(dal_instance):
    if dal_instance:
        dal_instance.clear_users()
        dal_instance.add_user('John', 'Doe', 'johndoe', 'jd@example.com')
        dal_instance.add_user('Jane', 'Doe', 'janedoe', 'jane@example.com')
        dal_instance.add_user('Winnie', 'Pooh', 'winnie', 'winnie@the.pooh')
        dal_instance.add_user('Bill', 'Norman', 'billie', 'billie@nor.man')

        print 'Searching for user billie'
        found_users = dal_instance.search_users('billie')

        print 'Search finished, found:'
        for user in found_users:
            print '\tUserName:{0} | FirstName:{1} | LastName:{2} | Email:{3}'.format(user.user_name, user.first_name, user.last_name, user.email)
        print


def run_app(should_run_init):
    if should_run_init:
        Init.init(engine)
    else:
        my_dal = DAL(engine)
        add_users(my_dal)
        all_users = my_dal.get_users()
        for user in all_users:
            print 'UserName:{0} | FirstName:{1} | LastName:{2} | Email:{3}'.format(user.user_name, user.first_name, user.last_name, user.email)


if __name__ == '__main__':
    #run_app(True)
    run_app(False)
