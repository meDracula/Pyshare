import socket
import pickle
from threading import Thread
from coderunner import test_code

HEADERSIZE = 10
HOST = socket.gethostname()
PORT = 8090

def package_payload(**kwargs):
    payload = pickle.dumps(kwargs)
    return bytes(f'{len(payload):<{HEADERSIZE}}', "utf-8") + payload

def unpackage_payload(payload):
    return pickle.loads(payload[HEADERSIZE:])

def client_connect(clientsocket):
            with clientsocket:
                full_payload = b''
                recving = True
                while True:
                    data = clientsocket.recv(1024)
                    if recving:
                        payload_length = int(data[:HEADERSIZE])
                        recving = False
                    full_payload += data

                    if len(full_payload)-HEADERSIZE == payload_length:
                        code_dict = unpackage_payload(full_payload)
                        recving = True
                        full_payload = b''

                        color = test_code(code_dict['test_code'], code_dict['solve_text'])
                        payload = package_payload(color=color)
                        clientsocket.send(payload)
                        clientsocket.close()
                        break


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            clientsocket, addr = s.accept()
            client_thread = Thread(target=client_connect, args=(clientsocket,))
            client_thread.start()
            client_thread.join()


if __name__ == '__main__':
    main()
