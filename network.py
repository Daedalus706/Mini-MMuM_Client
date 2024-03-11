from client import Client
import threading
import time


class Network:
    def __init__(self, address) -> None:

        self.client:Client = Client(address, 5010)
        self.data_list:list = []

        self.connected:bool = False

        self.start_thread = threading.Thread(target=threaded_connect, args=(self,))
        self.update_thread = threading.Thread(target=threaded_update_data, args=(self,))

        self.start_thread.start()

    def get_data(self) -> dict|None:
        if len(self.data_list) > 0:
            data = self.data_list[0]
            self.data_list = self.data_list[1:]
            return data
        else:
            return None
    
    def close(self):
        self.start_thread.do_run = False
        self.update_thread.do_run = False
        self.client.close()

    
def threaded_connect(network:Network):
    t = threading.current_thread()
    ctime = 0
    while getattr(t, "do_run", True):
        if time.time() > ctime+3:
            ctime = time.time()
            try:
                network.client.connect()
                network.connected = True
                print("Connected")
                network.update_thread.start()
                break
            except ConnectionRefusedError as e:
                print("Trying to connect...")
            except TimeoutError as e:
                print("Trying to connect...")


def threaded_update_data(network:Network):
    client = network.client
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        data = client.recive()
        network.data_list.append(data)
        if len(network.data_list) > 10:
            print(f"Warning: too much data in queue: {len(network.data_list)}")