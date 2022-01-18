from app.persistence.db import Document, db
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    collection = db.users

    @classmethod
    def create(cls, **data):
        user = User(data)
        user.password = data['password']
        return user

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, passwd):
        self.__dict__.update({'password': generate_password_hash(passwd)})

    @classmethod
    def verify_password(cls, password_hash, password):
        return check_password_hash(password_hash, password)

