import socket
HOST = '0.0.0.0'
PORT = 8090
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.bind((HOST, PORT))
   s.listen()
   conn, addr = s.accept()
   with conn:
       print('Connected by:', addr)
       while True:
           data = conn.recv(1024)
           print("Recived: ", repr(data))
           if not data:
               break
           conn.sendall(data)

