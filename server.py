import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostbyname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)