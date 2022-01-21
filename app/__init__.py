from dotenv import load_dotenv
from flask import Flask
from app.persistence.db import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    init_db(app)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix="/")

    from app.blueprints.admin import bp_admin
    app.register_blueprint(bp_admin)

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    from app.blueprints.users import bp_user
    app.register_blueprint(bp_user)

    return app


if __name__ == '__main__':
    load_dotenv()
    create_app().run()
