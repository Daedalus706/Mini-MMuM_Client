import json
import random
import time

from model import *
from service.events import Event




class GameService:
    def __init__(self, field_size:tuple[int, int]) -> None:
        self.round_time:float = 120.
        self.round_start:float = time.time()
        self.countdown:float = self.round_time

        self.map = Map(field_size)

        self.characters:list[Character] = []
        self.players:dict[str:Character] = {}

        self.active_character:Character = None
        self.temporary_active_character:Character = None
        self.selected_field:Field = None
        self.active_ability:Ability = None
        self.ability_queue_pos = 0

        self.events:list[Event] = []

        self.abilities = {}
        self.weapons = {}

        self.dice_roll_result:int = 0
        self.dice_to_roll:list[DICE] = []
        self.attack_stage = 'awaiting_data'     # possible stages: 'ready' 'ability'
        self.cooldown_targert:float = 0
        self.cooldown_start:float = 0

    def handle_data(self, data:dict[str:str]) -> None:
        if time.time() > self.round_start+self.round_time:
            self.next_character()

        if not self.check_cooldown_finnish():
            return
        
        if data == None:
            return
    
        print(f"Handleing data:", data)
        if 'request' in data:

            match data['request']:
                
                case 'abilities':
                    print("\n----------------------------------- Abilities ------------------------------------------------------")
                    for ability in data['data']:
                        name = ability[0]
                        cost = ability[1]
                        active = ability[2] != 0
                        bonus = ability[3] != 0
                        action = ability[4]
                        action_queue = json.loads(ability[5])
                        tags = json.loads(ability[6])
                        triggers = [TRIGGER.get_by_value(int(a)) for a in ability[7].split(',')]
                        
                        new_ability = Ability(name, cost, active, bonus, action, action_queue, tags, triggers)
                        self.abilities[name] = new_ability
                        print(new_ability)
                    print("---------------------------------------------------------------------------------------------------\n")
                
                case 'weapons':
                    print("\n----------------------------------- Weapons -------------------------------------------------------")
                    for weapon in data['data']:
                        name = weapon[0]
                        range = weapon[1]
                        one_handed = weapon[2] != 0
                        damage = weapon[3]
                        uses = weapon[4]
                        aoe_type = AOE.get_by_value(weapon[5])
                        tags = json.loads(weapon[6])
                        
                        new_weapon = Weapon(name, range, one_handed, damage, uses, aoe_type, tags)
                        self.weapons[name] = new_weapon
                        print(new_weapon)
                    print("---------------------------------------------------------------------------------------------------\n")
                    
                    #TODO remove
                    for character in self.characters:
                        character.weapon_slot0 = self.weapons['sword']
            
            self.attack_stage = 'ready'
            self.round_start = time.time()
                
        elif 'userName' in data:

            ### performs following actions only if the player is active
            if self.active_character == self.players[data['userName']]:

                ### Moves the player and reduces character's moves 
                if 'move' in data:
                    self.map.move(self.active_character, data['move'])
                
                ### Moves the field selection
                elif 'select' in data:
                    if data['select'] == 'center':
                        self.selected_field = self.map.get_pos_of(self.active_character)
                    else:
                        new_selection = self.map.get_neighbor(self.selected_field, data['select'])
                        if new_selection is not None:
                            self.selected_field = new_selection
                
                elif 'round' in data:
                    match data['round']:
                        ### Ends the current round
                        case 'end':
                            self.next_character()
                
                ### Uses ability
                elif 'ability' in data:
                    if self.attack_stage == 'ready':
                        ability = self.abilities[data['ability']]
                        self.use_ability(ability)
                
                ### rolls a dice
                elif 'dice' in data:
                    if self.attack_stage == 'ability':
                        self.roll_dice()
                        self.dice_to_roll = self.dice_to_roll[1:]
                        if len(self.dice_to_roll) == 0:
                            self.end_ability()

    def use_ability(self, ability:Ability):
        origin = self.map.get_pos_of(self.active_character)
        tags = ability.tags

        if not ability.bonus and self.active_character.get_actions() == 0:
            print("Ability: no actions left")
            return
        
        if ability.bonus and self.active_character.get_bonus_actions()+self.active_character.get_actions() == 0:
            print("Ability: no actions and bonus actions left")
            return
        
        if self.active_character.get_mp()-ability.cost < 0:
            print("Ability: not enough MP")
            return
        
        if 'weapon' in tags:
            weapon = self.active_character.get_weapon(tags['weapon'])
            if self.map.field_in_range(origin.get_pos(), self.selected_field, weapon.range):
                print("Ability: in range")
            else:
                print('Ability: not in range')
                return
        
        self.attack_stage = 'ability'
        self.active_ability = ability
        self.ability_queue_pos = 0
        match self.get_ability_queue_action():
            case 'ac_roll':
                self.dice_to_roll = DICE.D20
            case 'damage_roll':
                if 'weapon' in ability.tags:
                    self.dice_to_roll = DICE.get_by_string(self.active_character.get_weapon(tags['weapon']).damage.split('+')[0])
        
        self.events.append(Event.ReadyToRoll(self.dice_to_roll[0]))

        print("Ability has tags", tags)
    
    def end_ability(self):
        self.attack_stage = 'ready'
    

    def roll_dice(self):
        self.dice_roll_result = random.randint(1, self.dice_to_roll[0].value)
        self.events.append(Event.RollDice(self.dice_to_roll[0], self.dice_roll_result))
        self.start_cooldown(3)


    def trigger_all(self, trigger:TRIGGER):
        for character in self.characters:
            character.trigger(trigger)
    

    def next_character(self):
        self.active_character.trigger(TRIGGER.ROUND_END)
        index = self.characters.index(self.active_character) + 1
        if index == len(self.characters):
            index = 0
            #self.trigger_all(TRIGGER.ST)
        self.active_character = self.characters[index]
        self.active_character.trigger(TRIGGER.ROUND_START)
        self.selected_field = self.map.get_pos_of(self.active_character)

        self.attack_stage = 'ready'
        self.dice_to_roll = []
        self.round_start = time.time()
        print("new actice character")


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


    def get_ability_queue_action(self) -> str:
        """gets the current action in the ability action queue"""
        if self.ability_queue_pos < len(self.active_ability.action_queue):
            return self.active_ability.action_queue[self.ability_queue_pos]
        return ""

    def get_events(self) -> list[Event]:
        """Returns list of events. Calling this will empty the event list."""
        events = self.events
        self.events = []
        return events
    
    def start_cooldown(self, delay:float) -> None:
        self.cooldown_start = time.time()
        self.cooldown_targert = self.cooldown_start+delay

    def check_cooldown_finnish(self):
        return time.time() > self.cooldown_targert
            