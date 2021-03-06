from app.persistence.repository import user_repo


def create_new_user(username: str, email: str, password: str):
    return user_repo.create_new_user(username, email, password)


def login(user_identifier, password: str) -> bool:
    return user_repo.login(user_identifier, password)


def get_profile(user_identifier: str):
    return user_repo.get_user(user_identifier)


def search_users(**kwargs):
    return user_repo.get_users(**kwargs)


def delete_user(username):
    return user_repo.delete_users(username=username)


def logout_user() -> bool:
    return user_repo.logout()
