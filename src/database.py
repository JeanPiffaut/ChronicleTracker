import sqlalchemy as db
import os


def get_db_connection():
    engine = db.create_engine(
        f'mysql+mysqldb://{os.environ.get("MYSQL_USER")}:{os.environ.get("MYSQL_PASSWORD")}@{os.environ.get("MYSQL_HOST")}/{os.environ.get("MYSQL_DATABASE")}')

    # Try to establish a connection to the database
    conn = engine.connect()
    return conn
