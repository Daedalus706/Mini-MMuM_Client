from network import Network
from service.game_service import GameService
from service.start_service import StartService
from view.view import View

import time


address = "localhost"
#address = "game.magnus-rpg.de"

start_service = StartService()
game_service = GameService((10, 10))

network = Network(address)
view = View(start_service, game_service)


while view.running and view.stage == "start":
    start_service.handle_data(network.get_data())
    view.update()
    view.draw()

if view.running:
    network.request_data(['weapons', 'abilities'])

while view.running and view.stage == "game":
    game_service.handle_data(network.get_data())
    view.update()
    view.draw()

network.close()
view.close()