from flask import Flask
from flask_restful import Api

app = Flask(__name__)

if __name__ == '__main__':
    Api(app, catch_all_404s=True)
    app.run()
