import pygame
from game_service import GameService
from model import Map, Character, Field

import time


class View:
    def __init__(self, service:GameService) -> None:

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
        self.map_surf.fill(0x6e4930)
        for x in range(service.map.size[0]):
            for y in range(service.map.size[1]):
                pygame.draw.rect(self.map_surf, 0xb9a158, (5+x*100, 5+y*100, 95, 95), border_radius=5)

        ### Create Selected Field Surf
        self.selection_surf = pygame.Surface((105, 105))
        pygame.draw.rect(self.selection_surf, 0x5060a0, (0, 0, 105, 105), border_radius=15, width=7)
        self.selection_surf.set_colorkey(0)

        ### Create Game Canvas
        self.canvas_pos = (0, 0)
        self.canvas:pygame.Surface = pygame.Surface((1005, 1005))


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
                new_size = pygame.display.get_window_size()
                self.canvas_pos = (0, (new_size[1]-self.map_surf.get_height())//2)

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

    

    def draw(self) -> None:
        """Draws the new Frame on the screen"""
        ### checks if enough time has passed to draw the next frame. FPS is the target frame rate
        FPS = 60
        if time.time()-1/FPS < self.last_frame_update:
            return
        self.last_frame_update = time.time()
        
        ### clears the screen
        self.window.fill(0xb16a3b)

        ### draws the canvas on the screen
        self.draw_canvas()

        pygame.display.update()


    def close(self):
        pygame.quit()