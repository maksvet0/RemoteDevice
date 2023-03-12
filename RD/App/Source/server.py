import socket
from colorama import *

ip = socket.gethostname()
port = 15
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()
print(Fore.WHITE + Back.YELLOW + "[*]Data is listened!")
print(Style.RESET_ALL)
input()