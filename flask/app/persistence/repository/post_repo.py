from app.persistence.models import Post
from datetime import datetime

def create_new_post(title, title_hash, username, description, test_code):
    from app.persistence.repository.user_repo import append_posts
    post = Post.create(title=title, title_hash=title_hash, username=username,
            description=description, test_code=test_code, created=datetime.now())
    res = post.save().acknowledged
    if res == True:
        post = get_post(post.title)
        return append_posts(post).acknowledged
    return res


def search_post_title(title:str, skip:int, limit:int):
    return Post.text_search(title, skip, limit).full_or_none()


def latest_posts(skip: int, limit: int):
    return Post.latest(skip, limit).full_or_none()


def delete_posts(**kwargs):
    return Post.delete(**kwargs)


def get_post(title):
    return Post.find(title=title).first_or_none()


def get_post_hash(title_hash):
    return Post.find(title_hash=title_hash).first_or_none()

def post_solution(username, solution_code, post):
    from app.persistence.repository.user_repo import append_solution_code
    post.post_solution(username, datetime.now(), solution_code)
    post = get_post(post.title)
    return append_solution_code(post).acknowledged


def submit_comment(post, username, text):
    post.add_comment(username, text, datetime.now())

