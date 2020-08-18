import socket
from  settings import *
import  sys


data = "Hello world!"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:


    sock.connect((HOST, PORT))


    data = input()
    sock.send(bytes(data + '\n','utf-8'))

    recieved = str(sock.recv(1024),'utf-8')

    print(f"Sent: {data}")
    print(f"Recieved: {recieved}")

