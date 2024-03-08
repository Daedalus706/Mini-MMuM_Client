import socket
import json


class Client:
    def __init__(self, addr, port):
        self.ip = addr
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

    def connect(self):
        data = '{"sender": "client"}'.encode()
        self.socket.sendall(data)
    
    def recive(self):
        data = self.socket.recv(1024)
        if not data:
            return None
        string = data.decode("utf-8")
        return json.loads(string)

