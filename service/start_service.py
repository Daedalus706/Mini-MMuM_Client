from model import *
from service.events import Event
import json


class StartService:
    def __init__(self) -> None:
        self.characters:list[Character] = []
        self.players:dict[str: Character] = {}

        self.events:list[Event] = []        

    def handle_data(self, data:dict[str:str]) -> None:
        if data != None:
            print(f"Handleing data:", data)

            ### Checks if the username is not in player list. If so creates a new character and adds it
            if not data['userName'] in self.players:
                
                new_character = Character(f"{data['userName']}'s character", data['userName'], TEAM.PLAYER)
                self.events.append(Event.NewChraracter(new_character))
                
                self.players[data['userName']] = new_character
                self.characters.append(new_character)
                
                print("Player Joined: "+data['userName'])

    def can_start(self):
        if len(self.players) == 0:
            return False
        return True

    def get_characters(self) -> list[Character]:
        return self.characters
    
    def get_players(self) -> dict[str: Character]:
        return self.players
    
    def get_events(self) -> list[Event]:
        """Returns list of events. Calling this will empty the event list."""
        events = self.events
        self.events = []
        return events
