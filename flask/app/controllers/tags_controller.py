from app.persistence.repository import tags_repo


def create_new_tag(tag: str):
    return tags_repo.create_new_tag(tag)


def get_tag(tag: str):
    return tags_repo.get_tag(tag=tag)


def iter_tags(start: int, stop: int):
    return tags_repo.iter_tags(start, stop)


def delete_tag(tag: str):
    return tags_repo.delete_tag(tag)
