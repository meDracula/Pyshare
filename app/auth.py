from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/posts')
def posters():
    return render_template("posters.html")
