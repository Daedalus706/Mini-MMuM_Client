import pygame
from game_service import GameService
from model import Map, Character, Field

import time


class View:
    def __init__(self, service:GameService) -> None:

        self.service:GameService = service

        self.running:bool = True
        self.last_frame_update:int = 0

        self.resolution:tuple[int, int] = (1200, 1000)
        self.window = pygame.display.set_mode(self.resolution, flags=pygame.RESIZABLE)

        pygame.display.set_caption("Mini-MMuM")

        icon = pygame.image.load('favicon.ico')
        icon.set_colorkey(0)
        pygame.display.set_icon(icon)

        self.map_surf:pygame.Surface = pygame.Surface((1000, 1000))
        self.map_surf.fill(0x9f6326)
        for x in range(service.map.size[0]):
            for y in range(service.map.size[1]):
                pygame.draw.rect(self.map_surf, 0xc0b050, (5+x*99, 5+y*99, 95, 95))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                print("quit")
                return
    
    def draw(self):
        if time.time()-1/60 < self.last_frame_update:
            return
        self.last_frame_update = time.time()
        self.window.blit(self.map_surf, (0, 0))

        game_map:list[list[Field]] = self.service.map.map

        for row in game_map:
            for field in row:
                if field.character is None:
                    continue
                pos = (field.x*99+50, field.y*99+50)
                pygame.draw.circle(self.window, 0x805020, pos, 40)


        pygame.display.update()

    def close(self):
        pygame.quit()