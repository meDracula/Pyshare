from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import logout_user, login_required, current_user

bp_user = Blueprint('bp_user', __name__)

color = False
solve_text = ""

@bp_user.get('/logout')
def logout():
    logout_user()
    flash('You are now logged out')
    return redirect(url_for('bp_open.home'))


@bp_user.get('/account')
@login_required
def account():
    return render_template('account.html')

@bp_user.get('/posts/<title>/solve')
@login_required
def solve_thepost_get(title):
    from app.controllers.post_controller import get_post
    post = get_post(title)
    return render_template('solve.html', post=post, solve_text=solve_text, color=color)


@bp_user.post('/posts/<title>/solve')
@login_required
def solve_thepost_post(title):
    from app.controllers.post_controller import post_solution, get_post
    from app.controllers.code_controller import test_it
    post = get_post(title)

    global color
    user_text = request.form.get('solve_text')
    submit = request.form.get('final')

    color = test_it(post.test_code, user_text)

    if color:
        global solve_text
        solve_text = user_text
    else:
        flash("Your code is RED!!!")

    if submit:
        post_solution(current_user.username, solve_text, post)
        return redirect(url_for('bp_open.thepost_get', title=title))
    return render_template('solve.html', post=post, solve_text=solve_text, color=color)

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

    res = create_new_post( title, current_user.username, description, test_code)
    if res == 'title':
        flash(f'Your {res} is not unique!')
        return redirect(url_for('bp_user.create_post'))
    else:
        flash('Your Post have been created')
        return redirect(url_for('bp_open.posters_get'))

