from client import Client
import pygame
import numpy as np

address = "localhost"
address = "10.147.18.240"

client = Client(address, 5010)

resolution = np.array([500, 500])
window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

pos = resolution // 2
size = np.array([50, 50])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    data = {'move': 'no'}
    data = client.recive()
    
    if data is not None:
        if data['move'] == 'left':
            pos -= size[0]
        elif data['move'] == 'right':
            pos += size[0]
        elif data['move'] == 'up':
            pos -= size[1]
        elif data['move'] == 'down':
            pos += size[1]

    window.fill(0)
    pygame.draw.rect(window, 0xffffff, ((pos-size/2)[0], (pos-size/2)[1], size[0], size[1]))
    pygame.display.update()
    clock.tick(20)
    