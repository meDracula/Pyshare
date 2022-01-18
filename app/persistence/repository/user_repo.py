from app.persistence.models import User

def get_all_users():
    return User.all()

def get_user(username, email):
    return next(User.find(username=username, email=email))

def set_password(user, password:str):
    user.password = password

def create_new_user(username:str, email:str, password:str):
    user = User.create(username=username, email=email, password=password)
    user.save()

def verify_password(password_hash: str, password:str) -> bool:
    return User.verify_password( password_hash, password)

