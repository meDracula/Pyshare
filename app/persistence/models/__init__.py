from app.persistence.db import Document, db

class User(Document):
    print(db)
    collection = db.users
