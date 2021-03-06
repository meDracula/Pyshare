from flask import Blueprint, render_template, redirect, session, url_for, flash, request
from flask_login import login_required, current_user

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/logout')
def logout():
    from app.controllers.user_controller import logout_user

    logout_user()
    flash('You are now logged out')

    return redirect(url_for('bp_open.home'))


@bp_user.get('/account')
@login_required
def account_get():
    return render_template('account.html')


@bp_user.post('/account')
@login_required
def account_post():
    from app.controllers.user_controller import delete_user, logout_user

    delete = request.form.get('delete_user')

    if delete:
        delete_username = current_user.username
        logout_user()
        delete_user(delete_username)
        flash(f"User {delete_username} deleted!")

    return redirect(url_for('bp_open.home'))


@bp_user.get('/posts/<title_hash>/solve')
@login_required
def solve_thepost_get(title_hash):
    from app.controllers.post_controller import get_post_hash

    post = session.get('view_post', None)

    if post is None:
        post = get_post_hash(title_hash)

    color = False
    solve_text = session.get("solve_text", "")

    return render_template('solve.html', post=post, solve_text=solve_text, color=color)


@bp_user.post('/posts/<title_hash>/solve')
@login_required
def solve_thepost_post(title_hash):
    from app.controllers.post_controller import post_solution, get_post_hash
    from app.controllers.code_controller import testit

    post = session['view_post'] if session.get('view_post', None) is not None else get_post_hash(title_hash)

    user_text = request.form.get('solve_text')
    submit = request.form.get('final')

    color = testit(post.test_code, user_text)

    if not color:
        flash("Your code is RED!!!")

    if submit and session['solve_text'] == user_text:
        post_solution(current_user.username, session['solve_text'], post)
        session.pop('solve_text')
        session.pop('color')
        return redirect(url_for('bp_open.thepost_get', title_hash=title_hash))

    session['color'] = color
    session['solve_text'] = user_text

    return render_template('solve.html', post=post, solve_text=session.get('solve_text', ""), color=color)


@bp_user.get('/posts/create')
@login_required
def create_post():
    return render_template('createpost.html')


@bp_user.post('/posts/create')
@login_required
def create_post_post():
    from app.controllers.post_controller import create_new_post

    title = request.form.get('title')
    description = request.form.get('description')
    test_code = request.form.get('test_code')

    if description == 'Description':
        description = ""

    res = create_new_post(title, current_user.username, description, test_code)
    if res == 'title':
        flash(f'Your {res} is not unique!')
        return redirect(url_for('bp_user.create_post'))
    else:
        flash('Your Post have been created')
        return redirect(url_for('bp_open.posters_get'))
