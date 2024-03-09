import pygame
from game_service import GameService
from model import Map, Character

import time


class View:
    def __init__(self, service:GameService) -> None:

        self.running = True
        self.last_frame_update = 0

        self.resolution:tuple[int, int] = (1200, 1000)
        self.window = pygame.display.set_mode(self.resolution, flags=pygame.RESIZABLE)

        pygame.display.set_caption("Mini-MMuM")

        icon = pygame.image.load('favicon.ico')
        icon.set_colorkey(0)
        pygame.display.set_icon(icon)

        self.map_surf = pygame.Surface((1000, 1000))
        self.map_surf.fill(0x9f6326)
        for x in range(service.map.size[0]):
            for y in range(service.map.size[1]):
                pygame.draw.rect(self.map_surf, 0xc0b050, (5+x*99, 5+y*99, 95, 95))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
    
    def draw(self):
        if time.time()-1/60 < self.last_frame_update:
            return
        self.last_frame_update = time.time()
        self.window.blit(self.map_surf, (0, 0))
        pygame.display.update()