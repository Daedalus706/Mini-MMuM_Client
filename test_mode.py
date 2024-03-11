from model import *
from service.game_service import GameService
from view.view import View

import time


service = GameService((10, 10))
view = View()

ctime = time.time()
while view.running:

    if time.time()-1/60 > ctime:
        ctime = time.time()
        view.update()
        view.draw()


