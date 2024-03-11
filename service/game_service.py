from model import *
from service.events import Event
import json
import random


class GameService:
    def __init__(self, field_size:tuple[int, int]) -> None:
        self.map = Map(field_size)

        self.characters:list[Character] = []
        self.players:dict[str:Character] = {}

        self.active_character:Character = None
        self.temporary_active_character:Character = None
        self.selected_field:Field = None

        self.events:list[Event] = []

        self.abilities = {}

    def handle_data(self, data:dict[str:str]) -> None:
        if data != None:
            print(f"Handleing data:", data)

            if 'request' in data:
                match data['request']:
                    case 'abilities':
                        for ability in data['data']:
                            name = ability[0]
                            active = ability[1] != 0
                            triggers = [TRIGGER.get_by_value(int(a)) for a in ability[2].split(',')]
                            tags = [int(a) for a in ability[3].split(',')]

                            self.abilities[ability[0]] = Ability(name, active, triggers, tags)
                
            elif 'userName' in data:

                ### performs following actions only if the player is active
                if self.active_character == self.players[data['userName']]:

                    ### Moves the player and reduces character's moves 
                    if 'move' in data:
                        self.map.move(self.active_character, data['move'])
                    
                    if 'select' in data:
                        if data['select'] == 'center':
                            self.selected_field = self.map.get_pos_of(self.active_character)
                        else:
                            new_selection = self.map.get_neighbor(self.selected_field, data['select'])
                            if new_selection is not None:
                                self.selected_field = new_selection
    
    def next_character(self):
        pass


    def place_characters(self):
        player_positions = [
            (1, 3),(2, 3),(3, 3), 
            (1, 4),(2, 4),(3, 4),
            (1, 5),(2, 5),(3, 5),
            (1, 6),(2, 6),(3, 6),
            (1, 7),(2, 7),(3, 7)]
        enemy_positions = [
            (8, 3),(7, 3),(6, 3), 
            (8, 4),(7, 4),(6, 4),
            (8, 5),(7, 5),(6, 5),
            (8, 6),(7, 6),(6, 6),
            (8, 7),(7, 7),(6, 7)]
        
        for player in self.players:
            character = self.players[player]
            pos = player_positions[random.randint(0, len(player_positions)-1)]
            player_positions.remove(pos)
            self.map.place(character, pos[0], pos[1])


    
    def get_events(self) -> list[Event]:
        """Returns list of events. Calling this will empty the event list."""
        events = self.events
        self.events = []
        return events


    

