from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import logout_user, login_required

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/logout')
def logout():
    logout_user()
    flash('You are now logged out')
    return redirect(url_for('bp_open.home'))


@bp_user.get('/account')
@login_required
def account():
    return render_template('account.html')
