import os

from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.orm import sessionmaker


class Create:
    def execute(self, db_name):
        load_dotenv()
        engine = sqlalchemy.create_engine(
            f'mysql+mysqldb://{os.environ.get("MYSQL_USER")}:{os.environ.get("MYSQL_PASSWORD")}@' +
            f'{os.environ.get("MYSQL_HOST")}/{db_name}')

        Session = sessionmaker(engine)
        session = Session()
