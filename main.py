from client import Client
import threading
import pygame
import numpy as np

address = "localhost"
#address = "10.147.18.240"

client = Client(address, 5010)

try:
    client.connect()
except ConnectionRefusedError as e:
    print("Could not connect:", e)
    quit()

resolution = np.array([500, 500])
window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

pos = resolution // 2
size = np.array([50, 50])

return_dict = {'pos': pos}

def threaded_update_players(return_dict:dict, client:Client):
    t = threading.current_thread()
    while getattr(t, "do_run", True):

        data = client.recive()

        if data is not None:
            if data['move'] == 'left':
                return_dict['pos'][0] -= size[0]
            elif data['move'] == 'right':
                return_dict['pos'][0] += size[0]
            elif data['move'] == 'up':
                return_dict['pos'][1] -= size[1]
            elif data['move'] == 'down':
                return_dict['pos'][1] += size[1]

client_thread = threading.Thread(target=threaded_update_players, args=(return_dict, client))
client_thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            client_thread.do_run = False
            pygame.quit()
            quit()



    window.fill(0)
    pygame.draw.rect(window, 0xffffff, ((pos-size/2)[0], (pos-size/2)[1], size[0], size[1]))
    pygame.display.update()
    clock.tick(20)
    