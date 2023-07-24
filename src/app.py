from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from character import character_bp

load_dotenv()

app = Flask(__name__)

if __name__ == '__main__':
    Api(app, catch_all_404s=True)

    app.register_blueprint(character_bp)
    app.run()
