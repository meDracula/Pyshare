from app.persistence.models import User
from flask_login import login_user, logout_user, current_user
from datetime import datetime


def create_new_user(username:str, email:str, password:str):
    user = User.create(password, username=username, email=email, created=datetime.now())
    return user.save().acknowledged


def get_users(**kwargs):
    return User.find(**kwargs)


def get_user(user_identifier):
    return User.find_parallel(username=user_identifier, email=user_identifier).first_or_none()


def delete_users(**kwargs):
    return User.delete(**kwargs)


def login(user_identifier, password):
    user = User.find_parallel(username=user_identifier, email=user_identifier).first_or_none()
    if user is not None and User.verify_password(user.__dict__['password'], password):
        login_user(user)
        user.__dict__['last_active'] = datetime.now()
        return user.save().acknowledged
    return False

def logout():
    current_user.__dict__['last_active'] = datetime.now()
    current_user.save().acknowledged
    logout_user()

def append_posts(post):
    current_user.posts.append(post._id)
    return current_user.save()

def append_solution_code(post):
    for codes in post.solution_codes:
        if codes['username'] == current_user.username:
            solution_id = codes['solution_id']
            break
    current_user.solution_code.append({'post_id':post._id, 'solution_id': solution_id})
    return current_user.save()

