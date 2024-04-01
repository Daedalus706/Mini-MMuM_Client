import pygame
import time

from service.game_service import GameService
from service.start_service import StartService
from service.events import Event, EventType

from model import Map, Character, Field

from view.colors import Color
from view.scene import Scene
from view.game_scene import GameScene
from view.start_scene import StartScene


class View:
    def __init__(self, start_service:StartService, game_service:GameService) -> None:
        pygame.init()
        pygame.font.init()

        self.game_service:GameService = game_service
        self.start_service:StartService = start_service

        self.stage:str = "start"
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

        ### define Scenes
        self.start_scene:Scene = StartScene(self.window)
        self.game_scene:Scene = GameScene(game_service, self.window)


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

                self.game_scene.resize()
                self.start_scene.resize()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.stage == 'start' and self.start_service.can_start():
                        self.stage = 'game'
                        self.game_service.characters = self.start_service.get_characters()
                        self.game_service.players = self.start_service.get_players()
                        self.game_service.active_character = self.start_service.get_characters()[0]
                        self.game_service.place_characters()
                        self.game_service.selected_field = self.game_service.map.get_pos_of(self.game_service.active_character)
                        self.game_scene.add_characters()

        match self.stage:
            case 'start':

                for event in self.start_service.get_events():
                    if event.type == EventType.NEW_CHARACTER:
                        self.start_scene.new_character(event.character)

            case 'game':
        
                for event in self.game_service.get_events():
                    if event.type == EventType.ROLL_DICE:
                        self.game_scene.roll_dice(event.dice, event.number)

                


    def draw(self) -> None:
        """Draws the new Frame on the screen"""
        ### checks if enough time has passed to draw the next frame. FPS is the target frame rate
        FPS = 60
        if time.time()-1/FPS < self.last_frame_update:
            return
        self.last_frame_update = time.time()

        match self.stage:
            case 'start':
                self.start_scene.draw()
            case 'game':
                self.game_scene.draw()

        pygame.display.update()


    def close(self):
        pygame.quit()