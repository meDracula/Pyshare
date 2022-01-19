from dotenv import load_dotenv
from flask import Flask
from app.persistence.db import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    init_db(app)
    from .auth import auth

    app.register_blueprint(auth, url_prefix="/")

    return app


if __name__ == '__main__':
    load_dotenv()
    create_app().run()
