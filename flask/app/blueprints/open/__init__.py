from flask import Blueprint, render_template, request, session, redirect, url_for, flash, abort
from flask_login import current_user, login_required

bp_open = Blueprint('bp_open', __name__)

@bp_open.get('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('bp_user.account_get'))
    return redirect(url_for('bp_open.home'))

@bp_open.get('/about')
def about():
    return render_template('about.html')

@bp_open.get('/login')
def login_get():
    return render_template('login.html')

@bp_open.post('/login')
def login_post():
    from app.controllers.user_controller import login

    user_identifier = request.form.get('identifier')
    password = request.form.get('password')

    if login(user_identifier, password):
        return redirect('home')
    else:
        flash('Wrong Username/Email or password!')
        return redirect(url_for('bp_open.login_get'))

@bp_open.get('/home')
def home():
    return render_template('home.html')

@bp_open.get('/posts')
def posters_get():
    from app.controllers.post_controller import get_posts

    sort_type = request.args.get('sort_type', 'latest', type=str)
    search_text = request.args.get('search_text', '', type=str)
    page = request.args.get('page', 0, type=int)

    if current_user.is_authenticated:
        votes = [vote for vote in current_user.votes]

    posts = get_posts(sort_type, page, search=search_text)
    return render_template("posters.html", current_user=current_user, sort_type=sort_type, posts=posts, pagecount=page, search_text=search_text)

@bp_open.post('/posts')
def posters_post():
    from app.controllers.post_controller import get_posts

    page = request.args.get('page', 0, type=int)

    create = request.form.get('create')
    latest = request.form.get('latest')
    search_text = request.form.get('search')

    if create:
        return redirect(url_for('bp_user.create_post'))

    sort_type = "search" if search_text is not None and latest is None else "latest"
    return redirect(url_for('bp_open.posters_get', sort_type=sort_type, search_text=search_text, page=page))


@bp_open.get('/posts/<title_hash>')
def thepost_get(title_hash):
    from app.controllers.post_controller import get_post_hash

    post = get_post_hash(title_hash)

    if post is None:
        abort(404)

    if current_user.is_authenticated:
        session['view_post'] = post

    return render_template("thepost.html", post=post, current_user=current_user)


@bp_open.post('/posts/<title_hash>')
@login_required
def thepost_post(title_hash):
    from app.controllers.post_controller import submit_comment, delete_posts, get_post_hash

    comment = request.form.get('commenttext')
    user_try = request.form.get('try')
    delete_post = request.form.get('delete')

    post = session.get('view_post', None)
    if post is None:
        post = get_post_hash(title_hash)


    if comment:
        submit_comment(post, current_user.username, comment)

    if user_try:
        return redirect(url_for("bp_user.solve_thepost_get", title_hash=title_hash))

    if delete_post:
        delete_posts(post.title)
        flash("Post deleted")
        return redirect(url_for("bp_open.posters_get"))

    return redirect(url_for("bp_open.thepost_get", title_hash=title_hash))


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')

@bp_open.post('/signup')
def signup_post():
    from app.controllers.user_controller import create_new_user

    username = request.form.get("username")
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    result = create_new_user(username, email, password1)
    if result != True:
        flash(f"Not Unique {result}")
        return redirect(url_for('bp_open.signup_get'))
    else:
        return redirect(url_for('bp_open.login_get'))

@bp_open.get('/account')
def account_get():
    return render_template('account.html')
