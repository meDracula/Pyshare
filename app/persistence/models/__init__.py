from app.persistence.db import Document, db
from passlib.hash import argon2


class User(Document):
    collection = db.users

    @classmethod
    def create(cls, password, **data):
        user = User(data)
        user.password = password
        user.__dict__.update({'schema': 1, 'role': 'normie', 'last_active': data['created']})
        del password, data
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

class Post(Document):
    collection = db.posts

    @classmethod
    def create(cls, **data):
        post = Post(data)
        post.__dict__.update({'solved': False, 'schema': 1, "solution_codes": [], "comments": []})
        del data
        return post

"""
post = {
        _id: <id>,
        schema: <version-id>,
        title: <post-title>,
        username: <name>,
        created: date,
        tag: <type-tags>,
        complex-rating: <rating-score>,
        solved: boolean,
        test_code: "py code ...",
        solution_codes: [
                        {
                            soutlion_id: <post_id>+<solution_id>,
                            username: <name>,
                            submitted: Date(),
                            ranking: <ranking>,
                            solution_code: "py code ..."
                        }
                        ]
        comments: [
                    {
                            username: <name>,
                            coment: <text>,
                            submitted: Date()
                    }
                ]
        }
"""

