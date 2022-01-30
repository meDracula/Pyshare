from app.persistence.db import Document, db, ResultList
from passlib.hash import argon2


class User(Document):
    collection = db.users

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

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

    @classmethod
    def text_search(cls, search, limit):
        return ResultList(cls(item) for item in cls.collection.find(
            { "$text": { "$search": search }}, { "score": { "$meta": "textScore"}})
            .sort( "score", -1 ).limit(limit))

    @classmethod
    def iterate(cls, skip, limit):
        return ResultList(cls(item) for item in cls.collection.find().skip(skip).limit(limit))

    @classmethod
    def latest(cls, limit):
        return ResultList(cls(item) for item in cls.collection.find().sort('created', -1).limit(limit))

    def post_solution(self, username, created, solution_code):
        solve_dict = {'solution_id': len(self.solution_codes),  'username': username, 'submitted':created, 'solution_code': solution_code }
        self.solution_codes.append(solve_dict)
        self.save()

    def add_comment(self, username, text, submitted):
        self.comments.append({'username': username, 'comment': text, 'submitted': submitted})
        self.save()
