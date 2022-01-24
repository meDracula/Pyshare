from app.persistence.models import User
from datetime import datetime
from pprint import pprint


def get_all_users():
    return User.all()


def get_users(**kwargs):
    return User.find(**kwargs)


def set_password(user, password:str):
    user.password = password


def verify_user(username, email):
    if User.find(username=username, email=email).first_or_none() is not None:
        return True
    return False


def create_new_user(username:str, email:str, password:str):
    user = User.create(password, username=username, email=email, created=datetime.now())
    return user.save().acknowledged


def verify_password(password_hash: str, password:str) -> bool:
    return User.verify_password( password_hash, password)

def stat_find(**kwargs):
    result = User.find_explain(**kwargs)
    pprint(result)
