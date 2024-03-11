from network import Network
from service.game_service import GameService
from view.view import View

import time


address = "localhost"
address = "10.147.18.240"

network = Network(address)
service = GameService((10, 10))
view = View(service)


while view.running:
    service.handle_data(network.get_data())
    view.update()
    view.draw()

network.close()
view.close()