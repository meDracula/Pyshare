from dotenv import load_dotenv
from flask import Flask
from app.persistence.db import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    init_db(app)
    return app


if __name__ == '__main__':
    load_dotenv()
    create_app().run()

