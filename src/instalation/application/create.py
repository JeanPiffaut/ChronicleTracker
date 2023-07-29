import os
from dotenv import load_dotenv

from common.misc import get_database_session


class Create:
    def execute(self, db_name):
        load_dotenv()
        session = get_database_session(os.environ.get("MYSQL_USER"), os.environ.get("MYSQL_PASSWORD"),
                                       os.environ.get("MYSQL_HOST"), os.environ.get("MYSQL_DATABASE"))
