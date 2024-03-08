import socket


class Client:
    def __init__(self, addr, port):
        self.ip = addr
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def echo_message(self, message:str):
        self.socket.connect((self.ip, self.port))
        self.socket.sendall(message.encode())
        data = self.socket.recv(1024)
        print(f"Received {data!r}")


if __name__ == '__main__':
    client = Client("4.245.190.111", 5010)
    client.echo_message("test message")