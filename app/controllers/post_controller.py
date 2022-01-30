from app.persistence.repository import post_repo
from datetime import datetime

def create_new_post(title:str, username:str, description:str, test_code):
    return post_repo.create_new_post(title, username, description, test_code)

def search_title(title: str):
    return post_repo.search_post_title(title)

def iterate_posts(step: int, limit=10):
    assert isinstance(limit, int), "limit must be a INT"
    step *= 10
    return post_repo.iterate_posts(step, limit)

def latest_posts(limit=10):
    return post_repo.latest_posts(limit)

def delete_posts(title: str):
    return post_repo.delete_posts(title=title)

def get_post(title: str):
    return post_repo.get_post(title)

def post_solution(username:str, solution_code, post):
    return post_repo.post_solution(username, solution_code, post)

def submit_comment(title:str, username: str, text: str):
    post = post_repo.get_post(title)
    return post_repo.submit_comment(post, username, text)
