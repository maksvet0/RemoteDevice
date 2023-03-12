import socket

ip = "127.0.0.1"
port = 15
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()
while True:
    user, adr = server.accept()
    user.send(input().encode("utf-8"))
    data = user.recv(1024)
    print(data.decode("utf-8")) 