import json
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

def json_create():
    path = "utils/generate/"
    with open(path+'usernames.txt', 'r', encoding='utf-8') as username_rf:
        with open(path+'email.txt', 'r', encoding='utf-8') as email_rf:
            data = []
            password_len = 10
            for _ in range(100):
                username = username_rf.readline()
                email = email_rf.readline()
                password = "".join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(password_len))
                data.append({'username': username, 'email': email, 'password': password})

    #data = json.loads(str(data))
    with open(path+'users.json', 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == '__main__':
    json_create()
