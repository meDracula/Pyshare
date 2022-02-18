import socket
import pickle

HOST = None
PORT = None
HEADERSIZE = None


def init_testit(app):
    global HOST, PORT, HEADERSIZE
    HOST = app.config["TESTIT_HOST"]
    PORT = int(app.config["TESTIT_PORT"])
    HEADERSIZE = 10


def package_payload(**kwargs):
    payload = pickle.dumps(kwargs)
    return bytes(f'{len(payload):<{HEADERSIZE}}', "utf-8") + payload


def unpackage_payload(payload):
    return pickle.loads(payload[HEADERSIZE:])


def testit(test_code, solve_text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        payload = package_payload(test_code=test_code, solve_text=solve_text)
        s.send(payload)

        data = s.recv(1024)
        return unpackage_payload(data)['color']


def submit_code():
    pass
