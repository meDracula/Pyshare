from app.persistence.db import Document, db
from passlib.hash import argon2


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
        self.__dict__.update({'password': argon2.using(rounds=12).hash(passwd)})

    @classmethod
    def verify_password(cls, password_hash, password):
        return argon2.verify(password, password_hash)
