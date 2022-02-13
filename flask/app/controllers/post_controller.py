from app.persistence.repository import post_repo
from datetime import datetime

def create_new_post(title:str, username:str, description:str, test_code):
    title_hash = str(hash(title))
    return post_repo.create_new_post(title, title_hash, username, description, test_code)


def search_title(title: str):
    return post_repo.search_post_title(title)


def get_posts(sort_type: str, skip: int, limit=10, search=""):
    skip *= limit
    if sort_type == 'latest':
        return post_repo.latest_posts(skip, limit)
    elif sort_type == 'search':
        return post_repo.search_post_title(search, skip, limit)


def delete_posts(title: str):
    return post_repo.delete_posts(title=title)


def get_post(title: str):
    return post_repo.get_post(title)


def get_post_hash(title_hash):
    return post_repo.get_post_hash(title_hash)


def post_solution(username:str, solution_code, post):
    return post_repo.post_solution(username, solution_code, post)


def submit_comment(post, username: str, text: str):
    return post_repo.submit_comment(post, username, text)


def post_voting(title_hash, vote):
    from app.persistence.repository.user_repo import user_vote

    if vote == 1 or vote == -1:
        post = get_post_hash(title_hash)
        return post_repo.post_voting(post, vote) if user_vote(post, vote) else False
    else:
        return False

