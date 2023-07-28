import sqlalchemy as db
import os

from sqlalchemy.orm import sessionmaker

engine = db.create_engine(
    f'mysql+mysqldb://{os.environ.get("MYSQL_USER")}:{os.environ.get("MYSQL_PASSWORD")}@' +
    f'{os.environ.get("MYSQL_HOST")}/{os.environ.get("MYSQL_DATABASE")}')

Session = sessionmaker(engine)
session = Session()
