import pygame

from service.game_service import GameService


class Scene:
    def __init__(self, window:pygame.Surface):
        self.window = window
        self.resolution = window.get_size()

    def resize(self):
        self.resolution = self.window.get_size()

    def draw(self):
        pass
