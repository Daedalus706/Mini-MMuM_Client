from .ability import Ability
from .armor import Armor
from .weapon import Weapon
from .effect import Effect

from .trigger import TRIGGER
from .team import TEAM


class Character:
    def __init__(self, name:str, user:str, team:TEAM) -> None:
        self.name:str = name
        self.user: str = user
        self.team:TEAM = team
        self.armor:Armor = None

        self.base_hp:int = 50
        self.base_ac:int = 4
        self.base_mp:int = 6
        self.base_moves:int = 3
        self.base_actions:int = 2
        self.base_bonus_actions:int = 1
        self.base_reactions:int = 1

        self.hp:int = self.base_hp
        self.ac:int = self.base_ac
        self.mp:int = self.base_mp
        self.moves:int = self.base_moves
        self.actions:int = self.base_actions
        self.bonus_actions:int = self.base_bonus_actions
        self.reactions:int = self.base_reactions

        self.weapon_slot0 = None
        self.weapon_slot1 = None

        self.item_slot0 = None
        self.item_slot1 = None

        self.effects:list[Effect] = {}

    def trigger(self, trigger:TRIGGER) -> None:
        """Trigger players effects"""
        match trigger:
            case TRIGGER.ROUND_START:
                self.new_round()

        for effect in self.effects.copy():
            effect.do_trigger(trigger)
            if effect.remove:
                self.effects.remove()

        
    def new_round(self) -> None:
        """Reset temporary resources"""
        self.actions = self.base_actions
        self.bonus_actions = self.base_bonus_actions
        self.moves = self.base_moves
        self.reactions = self.base_reactions

    def execte_ability(self, ability:Ability, target) -> None:
        pass

    def can_move(self):
        if self.moves < 1:
            return False
        return True

    def move(self):
        self.moves -= 1

    def get_hp(self) -> int:
        return self.hp

    def get_ac(self) -> int:
        if self.armor is None:
            return self.ac
        return self.ac + self.armor.ac
    
    def get_mp(self) -> int:
        return self.mp
    
    def get_actions(self) -> int:
        return self.actions
    
    def get_bonus_actions(self) -> int:
        return self.base_bonus_actions
    
    def get_moves(self) -> int:
        return self.moves
    
    def get_weapon(self, weapon_slot:int) -> Weapon:
        if weapon_slot == 0:
            return self.weapon_slot0
        else:
            return self.weapon_slot1