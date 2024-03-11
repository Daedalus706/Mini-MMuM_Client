import pygame
from service.game_service import GameService
from model import Map, Character, Field
from view.character_info import CharacterInfo
from view.colors import Color
from service.events import Event, EventType

import time


class View:
    def __init__(self, service:GameService) -> None:
        pygame.init()
        pygame.font.init()

        self.service:GameService = service

        self.running:bool = True
        self.last_frame_update:int = 0

        ### Creating Window with dafault size (1505, 1005)
        self.resolution:tuple[int, int] = (1505, 1005)
        self.window = pygame.display.set_mode(self.resolution, flags=pygame.RESIZABLE)

        ### Setting up window title and icon
        pygame.display.set_caption("Mini-MMuM")
        icon = pygame.image.load('favicon.ico')
        icon.set_colorkey(0)
        pygame.display.set_icon(icon)

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

    def new_character(self, character:Character) -> None:
        """Call this whenever a new Character connects to the game"""
        width = self.resolution[0] - self.canvas.get_width() - 20
        self.character_info_dict[character] = CharacterInfo(character, width)


    def update(self):
        """handles the pygeme event queue. E.g. closes the window, handles resizes, etc."""
        for event in pygame.event.get():

            ### Checks if the Window gets closed. The acctual shutdown is managed in main.py
            if event.type == pygame.QUIT:
                self.running = False
                print("quit")
                return
            
            ### Handles window Resizes
            if event.type == pygame.VIDEORESIZE:
                self.resolution = pygame.display.get_window_size()
                self.canvas_pos = (0, (self.resolution[1]-self.map_surf.get_height())//2)
                width = self.resolution[0] - self.canvas.get_width() - 20
                for character in self.character_info_dict:
                    info:CharacterInfo = self.character_info_dict[character]
                    info.create_surf(width)
                    info.update_surf()
        
        for event in self.service.get_events():

            ### Handles new players
            if event.type == EventType.NEW_CHARACTER:
                self.new_character(event.character)
                

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

    

    def draw(self) -> None:
        """Draws the new Frame on the screen"""
        ### checks if enough time has passed to draw the next frame. FPS is the target frame rate
        FPS = 60
        if time.time()-1/FPS < self.last_frame_update:
            return
        self.last_frame_update = time.time()
        
        ### clears the screen
        self.window.fill(Color.COPPER)

        ### draws the canvas on the screen
        self.draw_canvas()

        ### draws the character info list 
        self.draw_info_list()

        pygame.display.update()


    def close(self):
        pygame.quit()