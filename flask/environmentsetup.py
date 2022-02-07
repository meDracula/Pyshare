import secrets

env = '.env'

key = secrets.token_hex()
key = 'SECRET_KEY='+key+"\n"

with open(env, 'r', encoding='UTF-8') as rf:
    data = rf.readlines()
    for index, line in enumerate(data):
        if "SECRET_KEY=" in line:
            data[index] = key

    with open(env, 'w', encoding='UTF-8') as wf:
        wf.writelines(data)

