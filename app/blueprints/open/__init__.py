from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
bp_open = Blueprint('bp_open', __name__)


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