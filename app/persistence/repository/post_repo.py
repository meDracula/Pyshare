from app.persistence.models import Post
from datetime import datetime

def create_new_post(title, username, description, test_code):
    post = Post.create(title=title, username=username, description=description, test_code=test_code, created=datetime.now())
    return post.save().acknowledged

def search_post_title(title, limit=10):
    return Post.text_search(title, limit).full_or_none()

def iterate_posts(skip:int, limit:int):
    return Post.iterate(skip, limit).full_or_none()

def latest_posts(limit: int):
    return Post.latest(limit).full_or_none()

def delete_posts(**kwargs):
    return Post.delete(**kwargs)

def get_post(title):
    return Post.find(title=title).first_or_none()

def post_solution(username, solution_code, post):
    return post.post_solution(username, datetime.now(), solution_code)

def submit_comment(post, username, text):
    post.add_comment(username, text, datetime.now())

