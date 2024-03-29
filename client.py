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
        data = '20      {"sender": "client"}'
        self.socket.sendall(data.encode())
    
    def recive(self) -> dict:
        try:
            header = self.socket.recv(HEADERSIZE)
            data = self.socket.recv(int(header.strip()))

            if not data:
                return None
            string = data.decode("utf-8")
            return json.loads(string)
        except ConnectionAbortedError:
            print("Connection closed")

    def request_from_server(self, request:str) -> None:
        message = json.dumps({'request': request, 'sender': 'client'})
        message = f'{len(message):<{HEADERSIZE}}' + message
        try:
            self.socket.sendall(message.encode())
            print("send request "+message)
        
        except Exception as e:
            print("failed to send request: ", e)

    
    def close(self):
        self.socket.close()
            

