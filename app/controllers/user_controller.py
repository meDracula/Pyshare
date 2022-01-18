from app.persistence.repository import user_repo

def get_all_users():
    return user_repo.get_all_users()

def get_user(username, email):
    return user_repo.get_user(username, email)

def create_new_user(username:str, email:str, password:str):
    return user_repo.create_new_user(username, email, password)

def verify_password(password_hash:str, password:str):
    return user_repo.verify_password(password_hash, password)
