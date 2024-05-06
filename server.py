import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostbyname("127.0.0.1")
PORT = 8000

s.bind((HOST_NAME, PORT))
s.listen(4)

while True:
    c, addr = s.accept()
    c.send(bytes("Hello, I am the server", "utf-8"))
    print(addr)