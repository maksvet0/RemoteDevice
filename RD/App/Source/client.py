import socket

ip = "127.0.0.1"
port = 15
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))
    client.send(input().encode("utf-8"))