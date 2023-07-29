from flask import Flask
from dotenv import load_dotenv
from character import character_bp
from common.misc import ExtendedApi

load_dotenv()

app = Flask(__name__)

if __name__ == '__main__':
    ExtendedApi(app, catch_all_404s=True)

    app.register_blueprint(character_bp)
    app.run(debug=True)
