import sqlalchemy
from flask_restful import Api
from sqlalchemy.orm import sessionmaker


def response_structure(code_status: int, response='', message=''):
    if 200 <= code_status < 300:
        status = 'Success'
    else:
        status = 'Error'

    args = dict()
    args['status'] = status
    args['message'] = message
    args['response'] = response

    return args, code_status


class ExtendedApi(Api):
    def handle_error(self, e):
        return response_structure(e.code, str(e))


def get_database_session(user, password, host, db_name):
    engine = sqlalchemy.create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db_name}')

    Session = sessionmaker(engine)
    session = Session()
    return session
