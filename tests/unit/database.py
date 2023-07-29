import os
from dotenv import load_dotenv
from common.misc import get_database_session

load_dotenv()

session = get_database_session(os.environ.get("MYSQL_USER"), os.environ.get("MYSQL_PASSWORD"),
                               os.environ.get("MYSQL_HOST"), os.environ.get("MYSQL_TEST_DATABASE"))
