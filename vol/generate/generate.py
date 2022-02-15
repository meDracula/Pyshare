import json
from os import path


def generate_users():
    from app.controllers.user_controller import create_new_user
    file_path = "/vol/generate/"
    file = "users.json"
    print("path:",path.exists(file_path), "file:", path.exists(file_path+file))
    with open(file_path+file, 'r', encoding="utf-8") as rf:
        data = json.load(rf)
    for user in data:
        res = create_new_user(user['username'], user['email'], user['password'])
        if res != True:
            print("NOT Unqiue, The error is in:", res, username, email)
            continue

if __name__ == '__main__':
    print("Generating 100 Users...")
    generate_users()
    print("... Complete!")
