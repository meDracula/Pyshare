from flask import Blueprint, render_template, redirect, url_for
from flask_login import logout_user

bp_user = Blueprint('bp_user', __name__)

@bp_user.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('bp_open.home'))

