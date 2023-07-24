from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import database

load_dotenv()

app = Flask(__name__)
database.get_db_connection()
if __name__ == '__main__':
    Api(app, catch_all_404s=True)
    app.run()
