import socketserver
from settings import *


class SimpleTCPserver(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()

       #print(f"{self.client_address} ")
        print(self.data)

        if self.data == "Who are you??":
            self.request.sendall("I`m Server")

        self.request.sendall(self.data.upper())


if __name__ == '__main__':
    with socketserver.TCPServer((HOST, PORT), SimpleTCPserver) as server:
        server.serve_forever()
