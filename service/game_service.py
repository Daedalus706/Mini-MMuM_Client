from model import *
from service.events import Event
import json


class GameService:
    def __init__(self, field_size:tuple[int, int]) -> None:
        self.map = Map(field_size)

        self.characters:list[Character] = []
        self.players:dict[str:Character] = {}

        self.active_character:Character = None
        self.selected_field:Field = None

        self.events:list[Event] = []

        self.abilities = {}

    def handle_data(self, data:dict[str:str]) -> None:
        if data != None:

            if 'request' in data:
                match data['request']:
                    case 'abilities':
                        for ability in data['data']:
                            name = ability[0]
                            active = ability[1] != 0
                            triggers = [TRIGGER.get_by_value(int(a)) for a in ability[2].split(',')]
                            tags = [int(a) for a in ability[3].split(',')]

                            self.abilities[ability[0]] = Ability(name, active, triggers, tags)
                        print(self.abilities)
                
            if 'userName' in data:
                if not data['userName'] in self.players:
                    new_character = Character(f"{data['userName']}'s character")
                    self.events.append(Event.NewChraracter(new_character))
                    
                    self.players[data['userName']] = new_character
                    self.characters.append(new_character)
                    self.active_character = new_character
                    for x in range(10):
                        if self.map.place(new_character, x, 0):
                            self.selected_field = self.map.get_pos_of(new_character)
                            break
            
                if 'move' in data:
                    character:Character = self.players[data['userName']]
                    self.map.move(character, data['move'])
                
                if 'select' in data:
                    if data['select'] == 'center':
                        self.selected_field = self.map.get_pos_of(self.active_character)
                    else:
                        new_selection = self.map.get_neighbor(self.selected_field, data['select'])
                        if new_selection is not None:
                            self.selected_field = new_selection
    
    def get_events(self) -> list[Event]:
        """Returns list of events. Calling this will empty the event list."""
        events = self.events
        self.events = []
        return events


    

