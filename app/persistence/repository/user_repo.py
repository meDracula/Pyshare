from app.persistence.models import User
from flask_login import login_user
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


def the_login_user(user_identifier, password):
    user = User.find_parallel(username=user_identifier, email=user_identifier).first_or_none()
    if user is not None and User.verify_password(user.__dict__['password'], password):
        login_user(user)
        user.__dict__['last_active'] = datetime.now()
        return user.save().acknowledged
    return False

