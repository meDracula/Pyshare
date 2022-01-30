from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash

bp_open = Blueprint('bp_open', __name__)

@bp_open.get('/')
def index():
    # if user is login then redirect to account page
    return redirect('home')

@bp_open.get('/login')
def login_get():
    return render_template('login.html')

@bp_open.post('/login')
def login_post():
    from app.controllers.user_controller import the_login_user

    user_identifier = request.form.get('identifier')
    password = request.form.get('password')

    if the_login_user(user_identifier, password):
        return redirect('home')
    else:
        flash('Wrong Username/Email or password!')
        return redirect(url_for('bp_open.login_get'))

@bp_open.get('/home')
def home():
    return render_template('home.html')

@bp_open.get('/posts')
def posters_get():
    from app.controllers.post_controller import latest_posts
    latest = latest_posts()
    sort_type = "Latest"
    return render_template("posters.html", sort_type=sort_type, posts=latest)

@bp_open.post('/posts')
def posters_post():
    from app.controllers.post_controller import search_title, latest_posts

    latest = request.form.get('latest')
    search_text = request.form.get('search')

    if search_text is not None and latest is None:
        posts = search_title(search_text)
        sort_type = "Search"
    else:
        posts = latest_posts()
        sort_type = "Latest"

    return render_template("posters.html", sort_type=sort_type, posts=posts)


@bp_open.get('/posts/<title>')
def thepost_get(title):
    from app.controllers.post_controller import get_post
    post = get_post(title)
    if post is None:
        abort(404)
    return render_template("thepost.html", post=post, current_user=current_user)


@bp_open.post('/posts/<title>')
@login_required
def thepost_post(title):
    user_try = request.form.get('try')
    if user_try:
        return redirect(url_for("bp_user.solve_thepost", title=title))
    return redirect(url_for("bp_open.thepost_get", title=title))


@bp_open.get('/sign-up')
def signup_get():
    return render_template('signup.html')

@bp_open.post('/signup')
def signup_post():
    username = request.form.get("user_name")
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    from app.persistence.models import User
    user = User.find(email=email).first_or_none()
    if user is not None:
        flash('Email already exists.', category='error')
    elif len(email) < 4:
        flash('Email must be greater than 3 characters.', category='error')
    elif len(username) < 4:
        flash('Username must be greater than 6 characters.', category='error')
    elif len(first_name) < 2:
        flash('First name must be greater than 1 character.', category='error')
    elif password1 != password2:
        flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
        flash('Password must be at least 7 characters.', category='error')
        return redirect(url_for('bp_open.signup_get'))

    user = User(
        {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': generate_password_hash(password1)
        }
    )
    user.save()
    return redirect(url_for('bp_open.login'))
