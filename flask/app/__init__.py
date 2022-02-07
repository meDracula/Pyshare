from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from app.persistence.db import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    init_db(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.controllers.user_controller import get_profile
        return get_profile(user_id)

    from app.blueprints.admin import bp_admin
    app.register_blueprint(bp_admin)

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    from app.blueprints.users import bp_user
    app.register_blueprint(bp_user)

    return app


load_dotenv()
app = create_app()
