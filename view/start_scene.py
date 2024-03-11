import pygame

from model import *
from view.colors import Color
from view.scene import Scene
from view.util import write_at


class StartScene(Scene):
    def __init__(self, window: pygame.Surface):
        super().__init__(window)

        self.font_h = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 100)
        self.font_p = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 25)

    def draw(self):
        self.window.fill(Color.BROWN)
        pygame.draw.rect(self.window, Color.GOLD, (15, 15, self.resolution[0]-30, self.resolution[1]-30), border_radius=20)

        write_at(self.window, self.font_h, (self.resolution[0]//2, 30), "Mini-MMuM", align='center')

