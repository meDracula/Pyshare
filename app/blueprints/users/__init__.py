from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import logout_user, login_required, current_user

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

@bp_user.get('/<title>/solve')
@login_required
def solve_thepost(title):
    from app.controllers.post_controller import post_solution, get_post
    post = get_post(title)
    solution_code = """
                    def func():
                        return 'hello world!'
                    """
    post_solution(current_user.username, solution_code, post)
    return redirect(url_for("bp_open.thepost_get", title=title))

