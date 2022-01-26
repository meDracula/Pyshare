from pymongo import MongoClient, errors
from abc import ABC

client = None
db = None


def init_db(app, show=False):
    """
    Set environment variables for the database in .env file in the project root directory.
    """
    global client, db
    username = app.config["DB_USER"]
    password = app.config["DB_PASSWORD"]
    host = app.config["DB_HOST"]
    port = int(app.config["DB_PORT"])
    database = app.config["DB_NAME"]
    client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
    db = client[database]

    if show:
        print(*[f"{cat} {status}\n" for cat, status in client.server_info().items()])
        print("Client: ", client)
        print("Databases:", client.list_database_names())
        print(f"{database} is a database:", database in client.list_database_names())


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None

    def full_or_none(self):
        return self if len(self) > 0 else None

    def nth_or_none(self, n, start=0):
        assert n >= start, "Variable start must me smaller than variable n"
        return self[start:n] if len(self) >= n else None


class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()
        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del (self.__dict__['_id'])
            try:
                return self.collection.insert_one(self.__dict__)
            except errors.DuplicateKeyError as e:
                setattr(e, 'acknowledged', list(e.details['keyPattern'].keys())[0])
                return e
        else:
            return self.collection.replace_one({'_id': self._id}, self.__dict__)

    def delete_field(self, field):
        self.collection.update_one({'_id': self._id}, {"$unset": {field: ""}})

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def find_parallel(cls, **kwargs):
        arr = [{key:kwargs[key]} for key in kwargs]
        return ResultList(cls(item) for item in cls.collection.find({ "$or": arr }))

    @classmethod
    def delete(cls, **kwargs):
        cls.collection.delete_many(kwargs)

