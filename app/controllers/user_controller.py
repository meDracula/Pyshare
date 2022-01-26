from app.persistence.repository import user_repo


def create_new_user(username:str, email:str, password:str):
    return user_repo.create_new_user(username, email, password)

def login_user(user_identifier, password: str) -> bool:
    return user_repo.login_user(user_identifier, password)

def get_profile(user_identifier: str):
    return user_repo.get_user(user_identifier)

def search_users(**kwargs):
    return user_repo.get_users(**kwargs)

def delete_user(user_identifier):
    return user_repo.delete_users()


def verify_user(username: str, email: str) -> bool:
    '''
        DEPRECATED function, REPLACED by login_user
        IF you are using this function change to another one.
        ALL DEPRECATED function will be replaced by the end of the weekend( jan 30 )
    '''
    print(f"WARNING: This function {verify_user.__name__} is deperecated!!!")
    return user_repo.verify_user(username, email)

def verify_password(password_hash:str, password:str):
    '''
        DEPRECATED function, REPLACED by login_user
        IF you are using this function change to another one.
        ALL DEPRECATED function will be replaced by the end of the weekend( jan 30 )
    '''
    print(f"WARNING: This function {verify_password.__name__} is deperecated!!!")
    return user_repo.verify_password(password_hash, password)

def get_users(**kwargs):
    '''
        DEPRECATED function, REPLACED by get_user_account and search_users
        IF you are using this function change to another one.
        ALL DEPRECATED function will be replaced by the end of the weekend( jan 30 )
    '''
    print(f"WARNING: This function {get_users.__name__} is deperecated!!!")
    return user_repo.get_users(**kwargs)

def get_all_users():
    '''
        DEPRECATED function, REPLACED by get_users()
        IF you are using this function change to another one.
        ALL DEPRECATED function will be replaced by the end of the weekend( jan 30 )
    '''
    print(f"WARNING: This function {get_all_users.__name__} is deperecated!!!")
    print("This function is also a DANGEROUS FUNCTION, DO NOT USE IF COLLECTION SIZE IS BIG")
    return user_repo.get_all_users()
