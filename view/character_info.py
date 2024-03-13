import pygame

from model import Character
from view.colors import Color
from view.util import write_at


class CharacterInfo:
    def __init__(self, character:Character, width:int) -> None:
        self.character = character

        if width < 20:
            width = 20
        self.width:int = width
        self.height_collabed:int = 45
        self.height_active:int = 300

        self.font_h = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 35)
        self.font_p = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 25)

        ### Creates the two surfaces and sets the colorkey to white (0xffffff) 
        self.surf_collabsed:pygame.Surface = None
        self.surf_active:pygame.Surface = None
        self.create_surf(self.width)
        self.update_surf()

    def create_surf(self, width:int) -> None:
        """Generates the surfaces according to the provided width. Call this everytime the window gets resized"""
        if width < 20:
            width = 20
        self.width = width
        self.surf_collabsed = pygame.Surface((self.width, self.height_collabed))
        self.surf_collabsed.set_colorkey(0xffffff)
        self.surf_collabsed.fill(0xffffff)
        self.surf_active = pygame.Surface((self.width, self.height_active))
        self.surf_active.set_colorkey(0xffffff)
        self.surf_active.fill(0xffffff)


    def update_surf(self) -> None:
        """Updates the surfaces. Call this everytime a stat of the provided character changes to display the change."""
        pygame.draw.rect(self.surf_collabsed, Color.GOLD, (0, 0, self.width, self.height_collabed), border_radius=10)
        pygame.draw.rect(self.surf_collabsed, Color.BROWN, (0, 0, self.width, self.height_collabed), border_radius=10, width=5)

        pygame.draw.rect(self.surf_active, Color.GOLD, (0, 0, self.width, self.height_active), border_radius=10)
        pygame.draw.rect(self.surf_active, Color.BROWN, (0, 0, self.width, self.height_active), border_radius=10, width=5)

        write_at(self.surf_collabsed, self.font_h, (10, 10), self.character.name, align='left')

        name_y, name_h = write_at(self.surf_active, self.font_h, (10, 10), self.character.name, align='left')[1::2]
        y, h = write_at(self.surf_active, self.font_p, (10, name_y+name_h+10), f"HP: {self.character.get_hp()}", align='left')[1::2]
        y, h = write_at(self.surf_active, self.font_p, (10, y+h+10), f"AC: {self.character.get_ac()}", align='left')[1::2]

        y, h = write_at(self.surf_active, self.font_p, (self.surf_active.get_width()-10, name_y+name_h+10), f"Bewegungen: {self.character.get_moves()}", align='right')[1::2]
        y, h = write_at(self.surf_active, self.font_p, (self.surf_active.get_width()-10, y+h+10), f"Aktionen: {self.character.get_actions()}", align='right')[1::2]
        y, h = write_at(self.surf_active, self.font_p, (self.surf_active.get_width()-10, y+h+10), f"Bonus Aktionen: {self.character.get_bonus_actions()}", align='right')[1::2]
        y, h = write_at(self.surf_active, self.font_p, (self.surf_active.get_width()-10, y+h+10), f"Magie Punkte: {self.character.get_mp()}", align='right')[1::2]


    def draw(self, surf:pygame.Surface, position:tuple[int,int], collabsed:bool=True) -> int:
        """Draws the info surface to the provided surface. It returns the bottom height coordinate"""
        surf.blit(self.surf_collabsed if collabsed else self.surf_active, position)
        return position[1]+(self.height_collabed if collabsed else self.height_active)
    
    


    