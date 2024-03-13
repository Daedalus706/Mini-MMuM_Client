import pygame

from model import *
from view.colors import Color
from view.scene import Scene
from view.util import write_at


class StartScene(Scene):
    def __init__(self, window: pygame.Surface):
        super().__init__(window)

        self.font_h = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 100)
        self.font_p = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 35)

        self.character_list:list[pygame.Surface] = []

    def new_character(self, character:Character):
        width = 300
        height = 60

        match character.team:
            case TEAM.PLAYER:
                color = 0
            case TEAM.ENEMY:
                color = 0xff5000
            case TEAM.HOSTILE:
                color = 0xa00000
            case TEAM.DEAD:
                color = 0x505050
            case _:
                raise ValueError(f"character has no valid team: {character.team}")

        surf = pygame.Surface((width, height))
        surf.set_colorkey(0xffffff)
        surf.fill(0xffffff)
        pygame.draw.rect(surf, Color.BROWN, (0, 0, width, height), border_radius=10)
        pygame.draw.rect(surf, Color.COPPER, (5, 5, width-10, height-10), border_radius=5)
        write_at(surf, self.font_p, (width//2, 20), character.name, text_color=color, align='center', background_color=Color.COPPER)

        self.character_list.append(surf)

    def draw(self):
        self.window.fill(Color.BROWN)
        pygame.draw.rect(self.window, Color.GOLD, (15, 15, self.resolution[0]-30, self.resolution[1]-30), border_radius=20)

        for surf, i in zip(self.character_list, range(len(self.character_list))):
            self.window.blit(surf, ((self.window.get_width()-surf.get_width())//2, 200+70*i))

        write_at(self.window, self.font_h, (self.resolution[0]//2, 30), "Mini-MMuM", align='center')

