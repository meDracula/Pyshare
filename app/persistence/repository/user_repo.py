from app.persistence.models import User


def get_all_users():
    return User.all()


def get_users(username, email):
    return User.find(username=username, email=email)


def set_password(user, password:str):
    user.password = password


def verify_user(username, email):
    if User.find(username=username, email=email).first_or_none() is not None:
        return True
    return False


def create_new_user(username:str, email:str, password:str):
    user = User.create(username=username, email=email, password=password)
    user.save()


def verify_password(password_hash: str, password:str) -> bool:
    return User.verify_password( password_hash, password)

