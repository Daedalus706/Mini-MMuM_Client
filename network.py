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

        self.request_threads:list[threading.Thread] = []

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
        for thread in self.request_threads:
            thread.do_run = False
        self.client.close()

    def request_abilities(self) -> None:
        """Sends a request for the abilities to the server. The response can be accesed in the data list with {'rquest': 'abilities', 'data': abilities}"""
        thread = threading.Thread(target=threaded_request, args=(self, 'abilities'))
        self.request_threads.append(thread)
        thread.start()
    
def threaded_connect(network:Network):
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        try:
            network.client.connect()
            network.connected = True
            network.update_thread.start()
            print("Connected")
            break
        except ConnectionRefusedError as e:
            print("Trying to connect...")
        except TimeoutError as e:
            print("Trying to connect...")
        time.sleep(3)


def threaded_update_data(network:Network):
    client = network.client
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        data = client.recive()
        network.data_list.append(data)
        if len(network.data_list) > 10:
            print(f"Warning: too much data in queue: {len(network.data_list)}")


def threaded_request(network:Network, request:str):
    client = network.client
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        if not network.connected:
            time.sleep(.1)
        else:
            client.request_from_server(request)
            network.request_threads.remove(t)
            break
        