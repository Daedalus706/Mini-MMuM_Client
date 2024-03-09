import socket
import json


HEADERSIZE = 8

class Client:
    def __init__(self, addr, port):
        self.ip = addr
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.ip, self.port))
        data = '20      {"sender": "client"}'.encode()
        self.socket.sendall(data)
    
    def recive(self):
        header = self.socket.recv(HEADERSIZE)
        data = self.socket.recv(int(header.strip()))

        if not data:
            return None
        string = data.decode("utf-8")
        return json.loads(string)
    
    def close(self):
        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except ConnectionAbortedError:
            print("Connection closed")

