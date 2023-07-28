import sqlalchemy as db
import os

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = db.create_engine(
    f'mysql+mysqldb://{os.environ.get("MYSQL_TEST_USER")}:{os.environ.get("MYSQL_TEST_PASSWORD")}@' +
    f'{os.environ.get("MYSQL_TEST_HOST")}/{os.environ.get("MYSQL_TEST_DATABASE")}')

Session = sessionmaker(engine)
session = Session()

session.connection()
