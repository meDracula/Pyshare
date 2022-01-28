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


def login_user(user_identifier, password):
    user = User.find_parallel(username=user_identifier, email=user_identifier).first_or_none()
    if user is not None and User.verify_password(user.__dict__['password'], password):
        login_user(user, user.__dict__['password'])
        user.__dict__['last_active'] = datetime.now()
        return user.save().acknowledged
    return False


# Repository deprecation block --->
def verify_user(username, email):
    if User.find(username=username, email=email).first_or_none() is not None:
        return True
    return False

def verify_password(password_hash: str, password:str) -> bool:
    return User.verify_password(password_hash, password)

def get_all_users():
    return User.all()
# <----
