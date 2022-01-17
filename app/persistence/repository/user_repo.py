from app.persistence.models import User

def get_all_users():
    return User.all()
