from dotenv import load_dotenv
from flask import Flask
from app.persistence.db import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    app.config["SECRET_KEY"] = "5121042174eccb4974405dfa4c4c00bc1337e8ec7638e5d1b9d151c07845ef0e"
    init_db(app)
    return app



if __name__ == '__main__':
    load_dotenv()
    create_app().run()

