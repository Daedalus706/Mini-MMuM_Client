import pygame

from model import Character
from view.colors import Color


class CharacterInfo:
    def __init__(self, character:Character, width:int) -> None:
        self.character = character

        if width < 20:
            width = 20
        self.width:int = width
        self.height_collabed:int = 50
        self.height_active:int = 400

        self.font = pygame.font.Font("fonts/MorrisRoman-Black.ttf", 30)

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

        surf = self.font.render(self.character.name, True, 0, Color.to_tuple(Color.GOLD))
        surf.set_colorkey(Color.to_tuple(Color.GOLD))
        self.surf_collabsed.blit(surf, ((self.surf_collabsed.get_width()-surf.get_width())/2, 10))
        self.surf_active.blit(surf, ((self.surf_active.get_width()-surf.get_width())/2, 10))

        


    def draw(self, surf:pygame.Surface, position:tuple[int,int], collabsed:bool=True) -> int:
        """Draws the info surface to the provided surface. It returns the bottom height coordinate"""
        surf.blit(self.surf_collabsed if collabsed else self.surf_active, position)
        return position[1]+(self.height_collabed if collabsed else self.height_active)