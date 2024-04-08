import pygame
import time
import math
import random
from model import DICE
from .util import write_at
from view.colors import Color

class DiceView:
    def __init__(self, delay:float=3., size=(100, 80), font_size=30) -> None:
        self.delay:float = delay
        self.size = size
        self.font_size = font_size

        self.dice = None
        self.start_time = 0
        self.pos = 0
        self.speed = 0

        self.font = pygame.font.Font("fonts/MorrisRoman-Black.ttf", font_size)
        self.surf = pygame.Surface(size)
        self.surf.fill(Color.GOLD)

        self.number_list:list[int] = []

    def setup(self, dice:DICE) -> None:
        """Sets the dice that is to be rolled"""
        self.reset()
        self.dice = dice

    def start_animation(self, number:int) -> None:
        """Starts the roll animation, that settles after the delay time on the provided number"""
        self.start_time = time.time()
        self.number_list = [random.randint(1, self.dice.value) for _ in range(random.randint(30, 40))]
        self.number_list.append(number)
        

        self.surf = pygame.Surface((self.size[0], (self.font_size+5)*(len(self.number_list)+1)))
        self.surf.fill(Color.GOLD)

        height = 0
        for n in self.number_list:
            write_at(self.surf, self.font, (self.size[0]//2, height), str(n), background_color=Color.GOLD, align='center')
            height += self.font_size+5

    def reset(self) -> None:
        """Empties the display"""
        self.dice = None
        self.surf = pygame.Surface(self.size)
        self.surf.fill(Color.GOLD)
        self.start_time = 0

    def draw(self, surf:pygame.Surface, pos:tuple[int,int]):

        temp_surf = pygame.Surface(self.size)
        temp_surf.fill(Color.GOLD)
        temp_surf.set_colorkey(0xffffff)

        if self.start_time != 0:
            time_passed = (time.time() - self.start_time) / self.delay
            if time_passed > 1:
                time_passed = 1

            #factor = math.sqrt(min(time_passed, 1))
            factor = -time_passed * (time_passed-2)

            height = int(factor * ((self.font_size+5)*(len(self.number_list)-1)  - self.font_size))
            temp_surf.blit(self.surf, (0, 0), area=(0, height, self.size[0], self.size[1]))
        else:
            text = "" if self.dice is None else f"D{self.dice.value}"
            write_at(temp_surf, self.font, (self.size[0]//2, self.size[1]//2-self.font_size//2), text, align='center')
        
        pygame.draw.rect(temp_surf, 0xffffff, (-10, -10, self.size[0]+20, self.size[1]+20), 10, 20)
        pygame.draw.rect(temp_surf, Color.BROWN, (0, 0, self.size[0], self.size[1]), 5, 10)

        surf.blit(temp_surf, pos)


