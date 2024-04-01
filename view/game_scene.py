import pygame

from model import *
from service.game_service import GameService
from view.character_info import CharacterInfo
from view.colors import Color
from view.scene import Scene
from view.dice_view import DiceView


class GameScene(Scene):
    def __init__(self, service: GameService, window: pygame.Surface):
        super().__init__(window)

        self.service = service

        ### Create Background Image
        self.map_surf:pygame.Surface = pygame.Surface((1005, 1005))
        self.map_surf.fill(Color.BROWN)
        for x in range(service.map.size[0]):
            for y in range(service.map.size[1]):
                pygame.draw.rect(self.map_surf, Color.GOLD, (5+x*100, 5+y*100, 95, 95), border_radius=5)

        ### Create Selected Field Surf
        self.selection_surf = pygame.Surface((105, 105))
        pygame.draw.rect(self.selection_surf, Color.LIGHT_BLUE, (0, 0, 105, 105), border_radius=15, width=7)
        self.selection_surf.set_colorkey(0)

        ### Create Game Canvas
        self.canvas_pos = (0, 0)
        self.canvas:pygame.Surface = pygame.Surface((1005, 1005))

        ### List of Character Info Elements
        self.character_info_dict:dict[Character: CharacterInfo] = {}

        ### Dice Box
        self.dice_box = DiceView()

    def resize(self):
        super().resize()

        self.canvas_pos = (0, (self.resolution[1]-self.map_surf.get_height())//2)
        width = self.resolution[0] - self.canvas.get_width() - 20
        for character in self.character_info_dict:
            info:CharacterInfo = self.character_info_dict[character]
            info.create_surf(width)
            info.update_surf()

    def draw(self):
        ### clears the screen
        self.window.fill(Color.COPPER)

        ### draws the canvas on the screen
        self.draw_canvas()

        ### draws the character info list 
        self.draw_info_list()

        ### draws the dice box
        self.dice_box.draw(self.window, (1200, 900))

    def draw_canvas(self) -> None:
        """ Redraws the canvas. This is function is called in the Map.draw() function and doesn't need to be called seperately """

        ### draws the background first
        self.canvas.blit(self.map_surf, (0, 0))

        ### Draws the selection outline
        if self.service.selected_field is not None:
            pos = (self.service.selected_field.x*100, self.service.selected_field.y*100)
            self.canvas.blit(self.selection_surf, pos)

        ### Draws all the characters to the game canvas
        game_map:list[list[Field]] = self.service.map.map
        for row in game_map:
            for field in row:
                if field.character is None:
                    continue
                pos = (field.x*100+53, field.y*100+53)
                pygame.draw.circle(self.canvas, 0x805020, pos, 40)

        ### Draws the canvas to the screen
        self.window.blit(self.canvas, self.canvas_pos)
    
    
    def draw_info_list(self) -> None:
        """draws the character info the the right side of the screen"""
        for c in self.character_info_dict:
            info:CharacterInfo = self.character_info_dict[c]
            info.update_surf()

        x = self.canvas.get_width() + 10
        y = 10
        for character in self.character_info_dict:
            info:CharacterInfo = self.character_info_dict[character]
            collabsed = character != self.service.active_character
            y = info.draw(self.window, (x, y), collabsed=collabsed) + 10

    def add_characters(self) -> None:
        for character in self.service.players.values():
            self.new_character(character)  
    
    def new_character(self, character:Character) -> None:
        """Call this whenever a new Character connects to the game"""
        width = self.resolution[0] - self.canvas.get_width() - 20
        self.character_info_dict[character] = CharacterInfo(character, width)

    def roll_dice(self, dice:DICE, number:int):
        """Starts the dice roll animation"""
        self.dice_box.start_animation(dice, number)