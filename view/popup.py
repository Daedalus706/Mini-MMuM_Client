import pygame
import time
from view.util import write_at


class Popup:
    def __init__(self, text:str, color:int, pos:tuple[int,int], delay:float=2) -> None:
        font = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 100)
        self.surf = font.render(text, True, color, background=1)
        self.surf.set_colorkey(1)

        self.start_time = time.time()
        self.pos = (pos[0]-self.surf.get_width()//2, pos[1]-self.surf.get_height()//2)
        self.active = True
        self.delay = delay

    def draw(self, window:pygame.Surface) -> None:
        fade = (self.delay + self.start_time() - time.time()) / self.delay
        if fade < 0:
            self.active = False
            return
        
        self.surf.set_alpha(int(255*fade))
        window.blit(self.surf, self.pos)
