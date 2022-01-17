from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "5121042174eccb4974405dfa4c4c00bc1337e8ec7638e5d1b9d151c07845ef0e"

    return app



if __name__ == '__main__':
    create_app().run()
