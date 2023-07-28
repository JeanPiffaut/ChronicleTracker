import os

from common.misc import get_database_session

session = get_database_session(os.environ.get("MYSQL_USER"), os.environ.get("MYSQL_PASSWORD"),
                               os.environ.get("MYSQL_HOST"), os.environ.get("MYSQL_DATABASE"))
