from app.persistence.repository import post_repo

def create_new_post(title:str, username:str, description:str, test_code):
    return post_repo.create_new_post(title=title, username=username, description=description, test_code=test_code)

def search_title(title: str):
    return post_repo.search_post_title(title)

def iterate_posts(step: int, limit=10):
    assert isinstance(limit, int), "limit must be a INT"
    step *= 10
    return post_repo.iterate_posts(step, limit)

def latest_posts(limit=10):
    return post_repo.latest_posts(limit)

